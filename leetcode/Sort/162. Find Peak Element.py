"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.

Follow up:
Your solution should be in logarithmic complexity.


Solution:
1. Linear Scan
2. Binary Search
"""


# Linear Scan
# Time: O(N), >97%, where N is the length of nums
# Space: O(1)
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return 0
        
        for i in range(l):
            if i == 0 and nums[i] > nums[i+1]:
                return i
            if i == l-1 and nums[i] > nums[i-1]:
                return i
            if nums[i-1] < nums[i] > nums[i+1]:
                return i


# Iterative Binary Search
# 一些关于 Binary Search 的心得：
# 要跳出循环，需要 left = mid + 1 or right = mid -1，i 与 j 的更新需要考虑仔细，有的时候需要保留 mid 在搜索范围内
# 最好把 nums[mid] 和其后面的数 nums[mid+1] 比，因为 mid = (i+j) // 2，是去尾的，mid-1会越界
# Time: O(logN), where N is the length of nums
# Space: O(1)
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return 0
        
        i, j = 0, l-1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] > nums[mid + 1]: # mid point is at a descending sequence, at leat a peak at leftside
                j = mid
            else:   # mid point is at a non-descending sequence, at least a peak at rightside
                i = mid + 1
        return i