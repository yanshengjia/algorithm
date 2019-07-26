"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3


Solution:
2 pointers
time-O(m+n)
space-O(m+n) 可以优化到 O(m), 保存一个 nums1[:m] 的拷贝，在 nums1 上直接改
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        i, j = 0, 0
        while i < m and j < n:
            n1 = nums1[i]
            n2 = nums2[j]
            if n1 < n2:
                res.append(n1)
                i += 1
            else:
                res.append(n2)
                j += 1
        if i < m:
            res.extend(nums1[i:m])
        if j < n:
            res.extend(nums2[j:n])
        nums1[:m+n] = res[:m+n]
