"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]


Solution:
1. Two set.
2. Built-in set intersection
"""


# Two set
# Time-O(n+m), O(n+m), where n and m are arrays' lengths. O(n) time is used to convert nums1 into set, O(m) time is used to convert nums2, and contains/in operations are O(1) in the average case.
# Space-O(n+m), in the worst case when all elements in the arrays are different.
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = set(nums1)
        n2 = set(nums2)
        res = []
        for n in n2:
            if n in n1:
                res.append(n)
        return res



# Built-in set intersection
# Time-O(n+m) in the average case and O(n×m) in the worst case when load factor is high enough.
# Space-O(n+m), in the worst case when all elements in the arrays are different.
class Solution(object):
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)