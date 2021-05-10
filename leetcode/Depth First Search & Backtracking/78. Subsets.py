"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]


Constraints:
* 1 <= nums.length <= 10
* -10 <= nums[i] <= 10
* All the numbers of nums are unique.


Solution:
Power set is all possible combinations of all possible lengths, from 0 to n.
* Loop over the length of combination
* Generate all combinations for a given length with Backtracking (DFS)

We define a backtrack function named backtrack(first, curr) which takes the index of first element to add and a current combination as arguments.
* If the current combination is done, we add the combination to the final output.
* Otherwise, we iterate over the indexes i from first to the length of the entire sequence n.
    * Add integer nums[i] into the current combination curr.
    * Proceed to add more integers into the combination : backtrack(i + 1, curr).
    * Backtrack by removing nums[i] from curr.

Notice:
* Use Python slicing to create a shallow copy of `cur_combo` and then append it to `res`, otherwise you will get nothing
"""


# Backtrack
# TC: O(N x x^N) to generate all subsets and then copy them into output list.
# SC: O(N). We are using O(N) space to maintain curr, and are modifying curr in-place with backtracking.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def backtrack(k, first_idx = 0, cur_combo = []):
            # if the current combination is done
            if len(cur_combo) == k:
                res.append(cur_combo[:])
                return
            
            for i in range(first_idx, n):
                # add nums[i] into current combination
                cur_combo.append(nums[i])
                # use next integers to complete the combination
                backtrack(k, i + 1, cur_combo)
                # backtrack
                cur_combo.pop()
        
        for k in range(n + 1):
            backtrack(k)
        return res
