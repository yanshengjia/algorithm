"""
Given an array nums sorted in non-decreasing order, and a number target, return True if and only if target is a majority element.

A majority element is an element that appears more than N/2 times in an array of length N.

 

Example 1:

Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
Output: true
Explanation: 
The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 > 9/2 is true.
Example 2:

Input: nums = [10,100,101,101], target = 101
Output: false
Explanation: 
The value 101 appears 2 times and the length of the array is 4.
Thus, 101 is not a majority element because 2 > 4/2 is false.


Solution:
1. Count the frequency of target
2. Binary Search to find the left / right bound of target
"""


# Binary Search
# Time: O(logN), N is the length of nums
# Space: O(1)
class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 1 and nums[0] != target:
            return False
        
        left, right = 0, 0
        
        # search the left bound
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i+j)//2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        left = i
        
        # search the right bound
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i+j)//2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] == target:
                i = mid
                if nums[i] == nums[i+1]:
                    i += 1
                else:
                    break
            else:
                j = mid - 1
        right = i
        
        return (right - left) + 1 > len(nums) / 2
        