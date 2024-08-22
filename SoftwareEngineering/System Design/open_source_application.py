
# https://aosabook.org/en/v2/distsys.html

import hashlib
import random
import threading
import time
from collections import defaultdict

class Cache:
    """
    A simple in-memory cache with a maximum size.
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
                # Remove a random item if cache is full (simple eviction strategy)
                self.cache.pop(random.choice(list(self.cache.keys())))
            self.cache[key] = value

class ConsistentHashRing:
    """
    A simple consistent hashing ring implementation.
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
    Simulates a distributed image storage system using consistent hashing.
    """

    def __init__(self, nodes=None, replicas=3):
        self.hash_ring = ConsistentHashRing(nodes, replicas)
        self.data = defaultdict(dict)  # {node: {image_id: image_data}}

    def upload_image(self, image_id, image_data):
        node = self.hash_ring.get_node(image_id)
        self.data[node][image_id] = image_data
        print(f"Image {image_id} uploaded to node {node}")

    def get_image(self, image_id):
        node = self.hash_ring.get_node(image_id)
        image_data = self.data[node].get(image_id)
        if image_data:
            print(f"Image {image_id} retrieved from node {node}")
            return image_data
        else:
            print(f"Image {image_id} not found")
            return None

# Example usage:
image_storage = ImageStorage(nodes=["node1", "node2", "node3"])

# Simulate image uploads
image_storage.upload_image("image1", "Data for image 1")
image_storage.upload_image("image2", "Data for image 2")
image_storage.upload_image("image3", "Data for image 3")

# Simulate image retrievals
image_storage.get_image("image2")
image_storage.get_image("image4")  # Not found