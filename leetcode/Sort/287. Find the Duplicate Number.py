"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3

Follow up:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.


Solution:
1. Hashtable
2. Soring
"""


# Hashtable
# Time: O(N)
# Space: O(N)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = dict()
        for n in nums:
            d[n] = d.get(n, 0) + 1
            if d[n] > 1:
                res = n
                break
        return n


# Sorting
# Time: O(NlogN)
# Space: O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
