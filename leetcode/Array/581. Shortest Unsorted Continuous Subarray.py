"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.


Solution:
1. Sort and Compare
2. Stack
"""


# Sorting
# Time: O(NlogN), N is the length of nums
# Space: O(N)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(nums)
        i, j = 0, len(nums) - 1
        while i < len(nums) and sorted_nums[i] == nums[i]:
            i += 1
        while j >= 0 and sorted_nums[j] == nums[j]:
            j -= 1
        if i >= j:
            return 0
        else:
            return j - i + 1
        