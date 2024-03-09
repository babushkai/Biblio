# Backtracking

## Explanation

Backtracking is an algorithmic technique for solving recursive problems by trying to build a solution incrementally and removing solutions that fail to satisfy the constraints of the problem at any point in time (hence "backtracking").

## Example Problems

- **N-Queens Problem:** Place N queens on an N×N chessboard so that no two queens threaten each other.
- **Permutations:** Find all permutations of a given set of numbers.

## Time Complexity

- The time complexity of backtracking algorithms can vary widely depending on the problem and the specific constraints. For some problems, it can be as high as O(N!), where N is the size of the input.

## Space Complexity

- The space complexity of backtracking algorithms is generally O(N) due to the recursion stack, where N is the recursion depth, often related to the size of the input.

## Implementation

```python
# Python implementation for Backtracking

def backtracking_template():
    def backtrack(path, selected, n):
        if len(path) == n:
            print(path)
            return
        for i in range(1, n + 1):
            if i not in selected:
                selected.add(i)
                backtrack(path + [i], selected, n)
                selected.remove(i)

    backtrack([], set(), 3)  # Example for n = 3
