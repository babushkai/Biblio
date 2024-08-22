import hashlib
import os
import random
import threading
from collections import defaultdict
from PIL import Image
import io

class Cache:
    """
    A thread-safe, in-memory cache with a maximum size. 
    """

    def __init__(self, max_size=1000):
        self.cache = {}
        self.max_size = max_size
        self.lock = threading.Lock()

    def get(self, key):
        with self.lock:
            return self.cache.get(key)

    def set(self, key, value):
        with self.lock:
            if len(self.cache) >= self.max_size:
                # Evict the least recently used item
                self.cache.pop(next(iter(self.cache)))
            self.cache[key] = value

class ConsistentHashRing:
    """
    Consistent hashing ring implementation for distributed systems.
    """

    def __init__(self, nodes=None, replicas=3):
        self.replicas = replicas
        self.ring = {}
        self.sorted_keys = []
        if nodes:
            for node in nodes:
                self.add_node(node)

    def _hash(self, key):
        return int(hashlib.sha256(key.encode()).hexdigest(), 16)

    def add_node(self, node):
        for i in range(self.replicas):
            key = self._hash(f"{node}-{i}")
            self.ring[key] = node
            self.sorted_keys.append(key)
        self.sorted_keys.sort()

    def remove_node(self, node):
        for i in range(self.replicas):
            key = self._hash(f"{node}-{i}")
            if key in self.ring:
                del self.ring[key]
                self.sorted_keys.remove(key)

    def get_node(self, key):
        if not self.ring:
            return None
        hashed_key = self._hash(key)
        for node_key in self.sorted_keys:
            if hashed_key <= node_key:
                return self.ring[node_key]
        return self.ring[self.sorted_keys[0]]

class ImageStorage:
    """
    A distributed image storage system using consistent hashing.
    Supports image file uploads and retrieval.
    """

    def __init__(self, nodes=None, replicas=3, storage_dir="storage"):
        self.hash_ring = ConsistentHashRing(nodes, replicas)
        self.data = defaultdict(dict)  # {node: {image_id: image_data}}
        self.cache = Cache(max_size=100)  # Optional cache to speed up reads
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def _save_image_to_disk(self, image_id, image_data, node):
        node_dir = os.path.join(self.storage_dir, node)
        os.makedirs(node_dir, exist_ok=True)
        image_path = os.path.join(node_dir, image_id)
        with open(image_path, 'wb') as f:
            f.write(image_data)

    def _load_image_from_disk(self, image_id, node):
        node_dir = os.path.join(self.storage_dir, node)
        image_path = os.path.join(node_dir, image_id)
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                return f.read()
        return None

    def upload_image(self, image_id, image_file):
        try:
            image_data = image_file.read()
            node = self.hash_ring.get_node(image_id)
            if node:
                self._save_image_to_disk(image_id, image_data, node)
                self.data[node][image_id] = image_data
                self.cache.set(image_id, image_data)  # Cache the uploaded image
                print(f"Image {image_id} uploaded to node {node}")
            else:
                print("No available nodes to store the image.")
        except Exception as e:
            print(f"Failed to upload image {image_id}: {e}")

    def get_image(self, image_id):
        try:
            # Check cache first
            cached_image = self.cache.get(image_id)
            if cached_image:
                print(f"Image {image_id} retrieved from cache")
                return cached_image

            node = self.hash_ring.get_node(image_id)
            if node:
                # Check in-memory storage
                image_data = self.data[node].get(image_id)
                if not image_data:
                    # If not in-memory, load from disk
                    image_data = self._load_image_from_disk(image_id, node)
                    if image_data:
                        self.cache.set(image_id, image_data)  # Cache the loaded image
                        self.data[node][image_id] = image_data  # Update in-memory data
                if image_data:
                    print(f"Image {image_id} retrieved from node {node}")
                    return image_data
                else:
                    print(f"Image {image_id} not found on node {node}")
            else:
                print("No available nodes to retrieve the image from.")
        except Exception as e:
            print(f"Failed to retrieve image {image_id}: {e}")
        return None

# Example usage:

# Initialize storage system with nodes
image_storage = ImageStorage(nodes=["node1", "node2", "node3"])

# Simulate image uploads
with open("image1.jpg", "rb") as img1:
    image_storage.upload_image("image1", img1)

with open("image2.jpg", "rb") as img2:
    image_storage.upload_image("image2", img2)

with open("image3.jpg", "rb") as img3:
    image_storage.upload_image("image3", img3)

# Simulate image retrievals
image_data = image_storage.get_image("image2")
if image_data:
    # To view the image using PIL
    image = Image.open(io.BytesIO(image_data))
    image.show()

image_data = image_storage.get_image("image4")  # Image not found
