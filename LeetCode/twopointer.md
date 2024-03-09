# Two Pointers Technique

## Explanation

The two pointers technique involves using two pointers to iterate through the data structure (like an array or list) to solve problems that require searching for a pair of elements or reordering elements in-place.

## Example Problems

- **Pair Sum:** Find two numbers in a sorted array that sum up to a specific target.
- **Squaring a Sorted Array:** Given an array sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

## Time Complexity

The time complexity of algorithms using the two pointers technique is generally O(n), as each element is visited at most once by each pointer.

## Space Complexity

The space complexity is typically O(1) as the technique doesn't require additional space proportional to the input size.

## Implementation

```python
# Python implementation for the two pointers technique
# Example: Pair Sum Problem

def pair_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left, right]  # Found the pair
        elif current_sum < target:
            left += 1  # Move the left pointer rightward
        else:
            right -= 1  # Move the right pointer leftward
    return [-1, -1]  # Pair not found
