def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    
    if m > 0 or n > 0:
        if m != 0:
            for i in range(n):
                nums1.pop(-1) # everytime, popping out index -1, moving the index -1              
            nums1.extend(nums2)
            nums1.sort()
        else:
            nums1.extend(nums2)
            for i in range(n):
                nums1.pop(0)   