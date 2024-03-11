# 1-D Dynamic Programming

## Explanation

1-D Dynamic Programming (DP) refers to solving problems by breaking them down into smaller subproblems and storing the solutions to these subproblems in a one-dimensional array. It avoids redundant calculations and is commonly used for optimization problems.

## Example Problems

- **Fibonacci Series:** Calculate the nth Fibonacci number.
- **Maximum Subarray Sum (Kadane's Algorithm):** Find the contiguous subarray with the maximum sum within a one-dimensional array.

## Time Complexity

- Time complexity for 1-D DP problems varies depending on the problem but is typically linear, O(n), where n is the size of the input, as you iterate through the array once.

## Space Complexity

The space complexity for 1-D DP is usually O(n), where n is the size of the input, since you need an array to store the results of subproblems.

# Python implementation for the Fibonacci Series using 1-D Dynamic Programming

def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n+1)  # 1-D DP array to store Fibonacci numbers
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Example usage:
if __name__ == "__main__":
    n = 10
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")

