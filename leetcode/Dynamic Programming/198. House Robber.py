"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.


Solution:
DP
在做 DP 问题时，需要清晰地定义问题以及递推公式中的变量。
可以从最简单的情况开始思考，N=1，2，3... 然后摸索出公式。

dp[i]: Largest amount that you can rob from the first i house, i starts from 1
A[i]: amount of money at ith house

dp[i] = max(dp[i-1], dp[i-2]+Ai)

At house i, basiclly you have 2 options:
* Ron the house i, and add its amount to dp[i-2] (why i-2? since if you rob house i, you cant rob house i-1)
* Do not rob the house i, and stick with the max amount of first i-1 houses, i.e. dp[i-1]
"""


# DP
# Time: O(N), >50%, where N is the length of nums
# Space: O(N)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        dp = [0] * l
        if l == 0:
            return 0
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums[0], nums[1])
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, l):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]


# DP
# Time: O(N), >95%, where N is the length of nums
# Space: O(1)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre, cur = 0, 0
        for n in nums:
            temp = cur
            cur = max(pre + n, cur)
            pre = temp
        return cur
