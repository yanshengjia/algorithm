"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


Solution:
1. Backtrackting
Here is a backtrack function which takes the index of the first integer to consider as an argument backtrack(first).

* If the first integer to consider has index n that means that the current permutation is done.
* Iterate over the integers from index first to index n - 1.
    * Place i-th integer first in the permutation, i.e. swap(nums[first], nums[i]).
    * Proceed to create all permutations which starts from i-th integer : backtrack(first + 1).
    * Now backtrack, i.e. swap(nums[first], nums[i]) back.
https://leetcode.com/problems/permutations/solution/

2. DFS
"""


# Time: better than O(N×N!) and a bit slower than O(N!)
# Space: O(N!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def backtrack(first = 0):
            # first represents the index of the first int in permutation
            if first == n:
                res.append(nums[:])     # deep copy nums[:] 
            for i in range(first, n):
                # place i-th int first in cur permutation
                nums[first], nums[i] = nums[i], nums[first]
                
                # use the next int to complete the permutations
                backtrack(first + 1)
                
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
            
        backtrack(0)
        return res