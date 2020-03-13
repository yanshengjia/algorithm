"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
Note: Length of the array will not exceed 10,000.


Solution:
Linear Scan
"""


# Scan
# Time: O(N), N is the length of nums
# Space: O(1)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        
        max_len = 1
        cur_len = 1
        for i in range(1, l):
            if nums[i] > nums[i-1]:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 1
        return max_len
