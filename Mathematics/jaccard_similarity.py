from sklearn.metrics import jaccard_score

# Example sets represented as binary vectors
set_a = np.array([1, 1, 1, 0, 0])
set_b = np.array([1, 1, 0, 1, 1])

# Compute Jaccard similarity using sklearn's jaccard_score (for binary vectors)
jac_sim = jaccard_score(set_a, set_b)
print(f"Jaccard similarity: {jac_sim}")

# Example sets of elements
set_a = {"apple", "banana", "orange"}
set_b = {"banana", "orange", "grape"}

# Compute Jaccard similarity
intersection = len(set_a.intersection(set_b))
union = len(set_a.union(set_b))
jac_sim = intersection / union
print(f"Jaccard similarity: {jac_sim}")