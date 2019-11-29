"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.


Solution:
Sliding Window
Consider the begin and the end of the winodw, count the number of potential windows with right-most index j.
"""


# Sliding Window
# Time: O(N), N is the length of nums
# Space: O(1)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        res = 0
        i = j = 0
        product = 1
        for j in range(len(nums)):
            product *= nums[j]
            while product >= k and i < len(nums):
                product /= nums[i]
                i += 1
            
            if i <= j:
                res += j - i + 1    # number of potential sliding windows with right-most index j
        return res


# Sliding Window
# Time: O(N), N is the length of nums
# Space: O(1)
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans