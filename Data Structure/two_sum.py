
"""
Time Complexity: Your approach has a time complexity of 
on2
n is the number of elements in nums. This is because you use a nested loop to compare each element with every other element to find a pair that adds up to the target. For each element in nums, you scan all other elements, leading to quadratic time complexity.
Space Complexity: The space complexity of your solution is 

on1
O(1) (constant space) because you're not using any additional data structures that grow with the input size. You only store a few pointers or indices at any time, regardless of the input array size.
"""
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i, e in enumerate(nums):
        for j, f in enumerate(nums):
            if i != j:
                sum_ = e+f
            else:
                continue
                
            if sum_ == target:
                return [i, j]
            else:
                continue

"""
Time Efficiency: The hash table solution is significantly more time-efficient for large arrays because it has a linear time complexity (
O(n))

O(n)) to store the indices of elements.
Practicality: For most practical purposes, especially with large datasets, the trade-off of using extra space is often worth the gain in time efficiency. The hash table approach is generally preferred due to its better time complexity.
"""
def twoSum(nums, target):
    # Dictionary to keep track of numbers and their indices
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

