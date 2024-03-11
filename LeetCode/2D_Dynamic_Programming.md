# 2-D Dynamic Programming

## Explanation

2-D Dynamic Programming (DP) extends the 1-D DP approach to two-dimensional problems. In 2-D DP, you store results in a two-dimensional array, with each dimension often representing a different attribute or decision axis.

## Example Problems

- **Knapsack Problem:** Given weights and values of items, put these items in a knapsack of a fixed capacity to get the maximum total value.
- **Edit Distance:** Find the minimum number of operations required to convert one string to another.

## Time Complexity

- The time complexity for 2-D DP problems is typically O(n*m), where n and m are the dimensions of the input, as you need to iterate through the two-dimensional array.

## Space Complexity

- The space complexity is O(n*m) to store the results of subproblems in a two-dimensional array.

## Implementation

```python
# Python implementation for the Knapsack Problem using 2-D Dynamic Programming

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                # Item i can be included
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                # Item i cannot be included
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

# Example usage:
if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    print(f"The maximum value in the knapsack of capacity {capacity} is: {knapsack(values, weights, capacity)}")
