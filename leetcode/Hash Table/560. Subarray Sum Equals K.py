"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2


Solution:
1. Brute Force Enumerate all subarray
2. Accumulative Sum
"""


# Brute Force
# Time: O(n^2)
# Space: O(1)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        
        for start in range(n):
            sum = 0
            for end in range(start, n):
                sum += nums[end]
                if sum == k:
                    res += 1
        return res


# Accumulative Sum
# Time: O(n^2)
# Space: O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        accumulative_sum = [0]
        s = 0
        for num in nums:
            s += num
            accumulative_sum.append(s)
        
        for start in range(n):
            sum = 0
            for end in range(start, n):
                if accumulative_sum[end+1] - accumulative_sum[start] == k:
                    res += 1
        return res


# Hashtable  (sum_i, number of occurences of sum_i)
# check if sum_i - k has occured already, if it is, there is a match, we get the value of key: sum_i - k
# Time: O(n)
# Space: O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        s = 0
        
        d = {0:1}   # key: accmulative sum_i, value: number of occurence of sum_i
        
        for i in range(n):
            s += nums[i]
            if s - k in d:
                res += d[s-k]
            d[s] = d.get(s, 0) + 1
        return res
        