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