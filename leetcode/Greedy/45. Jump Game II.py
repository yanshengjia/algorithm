"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.


Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2


Constraints:
* 1 <= nums.length <= 104
* 0 <= nums[i] <= 1000


Solution:
BFS inspried greedy problem

For every jump, not jump as far as you can, jump with the max jump power.

The main idea is based on greedy. 
Let's say the range of the current jump is [curBegin, curEnd], 
curFarthest is the farthest point that all points in [curBegin, curEnd] can reach. 
Once the current point reaches curEnd, then trigger another jump, and set the new curEnd with curFarthest,
then keep the above steps.
"""


# (Kinda BFS) Greedy
# TC: O(N), N = len(nums), since we visit each elemnet in the array only once
# SC: O(1) 
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        cur_jump_end = 0
        farthest = 0
        
        for i in range(len(nums) - 1):
            # continumsly find how far we can reach in the current jump
            farthest = max(farthest, i + nums[i])
            
            # if we come to te end of current jump
            # trigger another jump
            if i == cur_jump_end:
                jumps += 1
                cur_jump_end = farthest
        return jumps
