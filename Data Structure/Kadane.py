def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    global maxSum
    maxSum = -10000
    def kadanes(prevSum, curElem):
        global maxSum
        maxSum = max(curElem, maxSum+curElem)
        return max(prevSum,maxSum)
    return reduce(kadanes, nums,-10000)