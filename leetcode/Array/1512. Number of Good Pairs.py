"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.


Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:
* 1 <= nums.length <= 100
* 1 <= nums[i] <= 100


Solution:
Use an array `count` to store the occurrence of each elements.
For each new element `a`, there will be more `count[a]` pairs

For example,
[1, 1, 1]
res = 0 + 1 + 2
"""


# Array
# Time: O(N), N is the length of nums
# Space: O(N)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = [0] * 101
        res = 0
        for n in nums:
            res += count[n]
            count[n] += 1
        return res
