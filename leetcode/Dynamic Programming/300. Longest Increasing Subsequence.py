"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.

Follow up:
* Could you improve it to O(n log n) time complexity?
* Output the LIS


Solution:
1. DP
dp[i]: the len of LIS ends with nums[i]  以 nums[i] 结尾的 LIS 长度，必须取到 nums[i]，不然之后不好比较
dp[i] = max(dp[j] + 1), j = [0, i-1] and nums[i] > nums[j]

res = max(dp[0], dp[1], ... dp[n-1])
"""


# DP
# Time: O(N^2)
# Space: O()
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0 or l == 1:
            return l
        
        dp = [1 for _ in range(l)]     # dp[i]: LIS ends at nums[i]
        
        max_len = 1
        for j in range(1, l):
            cur_len = 1
            for i in range(j):
                if nums[j] > nums[i]:
                    if dp[i] + 1 > cur_len:
                        cur_len = dp[i] + 1
            dp[j] = cur_len
        return max(dp)


# Output LIS string as well
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0 or l == 1:
            return l
        
        dp = [1 for _ in range(l)]          # dp[i]: LIS ends at nums[i], include nums[i]
        lis = [[i] for i in range(l)]       # LIS string ends at nums[i], include nums[i]
        
        max_len = 1
        for j in range(1, l):
            cur_len = 1
            for i in range(j):
                if nums[j] > nums[i]:
                    if dp[i] + 1 > cur_len:
                        cur_len = dp[i] + 1
                        lis[j] = lis[i] + [j]
            dp[j] = cur_len
        
        # get LIS string
        lis_len = 0
        for i in range(l):
            if len(lis[i]) > lis_len:
                lis_len = len(lis[i])
                max_lis = lis[i]
        print(max_lis)
        return max(dp)