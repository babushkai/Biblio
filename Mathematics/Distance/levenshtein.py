def levenshtein_distance(s1, s2):
    """Computes the Levenshtein distance between two strings.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        int: The Levenshtein distance between s1 and s2.
    """

    # Create a matrix to store the distances between the substrings of s1 and s2
    distance_matrix = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    # Initialize the first row and column of the matrix
    for i in range(len(s1) + 1):
        distance_matrix[i][0] = i
    for j in range(len(s2) + 1):
        distance_matrix[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            # If the characters match, no cost
            if s1[i-1] == s2[j-1]:
                cost = 0
            # Otherwise, the cost is 1
            else:
                cost = 1

            # Compute the minimum cost of insertion, deletion, or substitution
            distance_matrix[i][j] = min(
                distance_matrix[i-1][j] + 1,  # Cost of insertion
                distance_matrix[i][j-1] + 1,  # Cost of deletion
                distance_matrix[i-1][j-1] + cost  # Cost of substitution
            )

    # Return the Levenshtein distance
    return distance_matrix[len(s1)][len(s2)]


# Example usage
s1 = "kitten"
s2 = "sitting"

distance = levenshtein_distance(s1, s2)
print(f"The Levenshtein distance between '{s1}' and '{s2}' is: {distance}")

# Output:
# The Levenshtein distance between 'kitten' and 'sitting' is: 3

