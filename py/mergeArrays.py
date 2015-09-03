"""
Merge Sorted Arrays
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""


def merge(nums1, m, nums2, n):
    if n == 0:
        return
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    indexNums1 = 0
    mIndex = n 
    nIndex = 0
    place = 0
    for counter in range(m - 1, -1, -1):
        nums1[m + n - 1 - ((m-1) - counter)] = nums1[counter]
        nums1[counter] = None

    while (nIndex < n) and (mIndex < m + n):
        if nums1[mIndex] <= nums2[nIndex]:
            nums1[place] = nums1[mIndex]
            mIndex += 1
        else:
            nums1[place] = nums2[nIndex] 
            nIndex += 1
        place += 1
    
    while (nIndex < n):
        nums1[place] = nums2[nIndex]
        nIndex += 1
        place += 1
    
    

