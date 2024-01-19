import numpy as np

class HilbertSpace:
    def __init__(self, inner_product):
        """
        Initializes a Hilbert space with the given inner product.

        Args:
            inner_product: A function that takes two vectors as input and returns their inner product.
        """
        self.inner_product = inner_product

    def norm(self, vector):
        """
        Computes the norm of a vector in the Hilbert space.

        Args:
            vector: The vector whose norm is to be computed.

        Returns:
            The norm of the vector.
        """
        return np.sqrt(self.inner_product(vector, vector))

    def distance(self, vector1, vector2):
        """
        Computes the distance between two vectors in the Hilbert space.

        Args:
            vector1: The first vector.
            vector2: The second vector.

        Returns:
            The distance between the two vectors.
        """
        return self.norm(vector1 - vector2)

    def is_orthogonal(self, vector1, vector2):
        """
        Checks if two vectors are orthogonal (perpendicular) in the Hilbert space.

        Args:
            vector1: The first vector.
            vector2: The second vector.

        Returns:
            True if the vectors are orthogonal, False otherwise.
        """
        return np.isclose(self.inner_product(vector1, vector2), 0)


# Example usage

# Define an inner product for a space of complex-valued functions on the interval [0, 1]
def inner_product(f, g):
    return np.dot(f, np.conj(g)) * np.diff(np.linspace(0, 1, len(f)))

# Create a Hilbert space with the given inner product
hilbert_space = HilbertSpace(inner_product)

# Define two functions
f = lambda x: np.exp(-x**2)
g = lambda x: np.sin(2 * np.pi * x)

# Compute the norm of each function
norm_f = hilbert_space.norm(f)
norm_g = hilbert_space.norm(g)

# Compute the distance between the two functions
distance = hilbert_space.distance(f, g)

# Check if the functions are orthogonal
is_orthogonal = hilbert_space.is_orthogonal(f, g)

print(f"Norm of f: {norm_f}")
print(f"Norm of g: {norm_g}")
print(f"Distance between f and g: {distance}")
print(f"Are f and g orthogonal? {is_orthogonal}")