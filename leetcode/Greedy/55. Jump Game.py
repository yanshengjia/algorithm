"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.


Solution:
1. Backtracking
2. DP
3. Greedy
"""

# Greedy
# Time: O(N), N is the length of nums
# Space: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = 0
        
        for idx, distance in enumerate(nums):
            # we can not reach current idx
            if can_reach < idx:
                return False
            
            # update can_reach index for cur idx
            can_reach = max(can_reach, idx + distance)
            
            # we already can reach the last index
            if can_reach >= len(nums) - 1:
                return True
        return False
        
        
