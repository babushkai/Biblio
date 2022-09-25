from typing import List

def singleNumber(self, nums: List[int]) -> int:
    from collections import Counter
    frequency = Counter(nums)
    return frequency.most_common()[-1][0]