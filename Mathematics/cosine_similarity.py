from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Example vectors
vector_a = np.array([1, 2, 3, 4, 5])
vector_b = np.array([2, 3, 4, 5, 6])

# Compute cosine similarity
cos_sim = cosine_similarity([vector_a], [vector_b])
print(f"Cosine similarity: {cos_sim[0][0]}")
