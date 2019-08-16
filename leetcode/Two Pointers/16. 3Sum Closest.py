"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Solution:
1. two pointers
"""


# Two Pointers
# Time: O(N^2), where N is the length of nums
# Space: O(1)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        res = 0
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < diff:
                    diff = abs(s - target)
                    res = s
                if s == target:
                    return target
                elif s > target:
                    k -= 1
                    while j < k-1 and nums[k] == nums[k-1]: # jump duplicates
                        k -= 1
                else:
                    j += 1
                    while j < k-1 and nums[j] == nums[j+1]: # jump duplicates
                        j += 1  
        return res
        