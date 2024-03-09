# Binary Search

## Explanation

Binary Search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item until you've narrowed the possible locations to just one.

## Example Problems

- **Finding an Element:** Determine if a target element exists within a sorted array.
- **Finding the First Occurrence:** In an array of duplicates, find the index of the first occurrence of a target element.

## Time Complexity

The time complexity of Binary Search is O(log n), where n is the number of elements in the input array. This is because the algorithm divides the search interval in half with each step.

## Space Complexity

The space complexity is O(1) when using an iterative approach since it maintains only a constant amount of space for pointers or indices.

## Implementation

```python
# Python implementation for Binary Search

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid  # Target found
        elif nums[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    return -1  # Target not found
