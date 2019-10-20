"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


# Time: O(N)
# Space: O(N)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            d[target - nums[i]] = i
        
        res = []
        for i in range(len(nums)):
            if nums[i] in d and i != d[nums[i]]:
                res.append(i)
                res.append(d[nums[i]])
                break
        return res
        