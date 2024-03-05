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

def twoSum(nums, target):
    # Dictionary to keep track of numbers and their indices
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

