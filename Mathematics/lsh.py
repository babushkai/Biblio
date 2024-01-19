import numpy as np
import hashlib

class LSH:
    def __init__(self, num_hash_tables, num_hash_functions, input_dim):
        self.num_hash_tables = num_hash_tables
        self.num_hash_functions = num_hash_functions
        self.input_dim = input_dim
        self.hash_tables = [{} for _ in range(num_hash_tables)]

    def hash(self, vector):
        hashes = []
        for _ in range(self.num_hash_functions):
            # Generate a random hyperplane
            weights = np.random.randn(self.input_dim)
            # Project the vector onto the hyperplane
            projection = np.dot(weights, vector)
            # Hash the projection
            hash_value = hashlib.sha1(str(projection).encode('utf-8')).hexdigest()
            hashes.append(hash_value)
        return hashes

    def insert(self, vector, label):
        hashes = self.hash(vector)
        for i, hash_value in enumerate(hashes):
            bucket = self.hash_tables[i].get(hash_value, set())
            bucket.add(label)
            self.hash_tables[i][hash_value] = bucket

    def search(self, query_vector, num_results):
        hashes = self.hash(query_vector)
        candidates = set()
        for i, hash_value in enumerate(hashes):
            bucket = self.hash_tables[i].get(hash_value, set())
            candidates.update(bucket)
        return sorted(candidates, key=lambda x: np.linalg.norm(query_vector - x))[:num_results]

        