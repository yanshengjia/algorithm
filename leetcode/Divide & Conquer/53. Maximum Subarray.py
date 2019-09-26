"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


Solution:
https://leetcode.com/problems/maximum-subarray/solution/

1. Divide and Conquer (like mergesort)
Let's follow here a solution template for the divide and conquer problems :
* Define the base case(s).
* Split the problem into subproblems and solve them recursively.
* Merge the solutions for the subproblems to obtain the solution for the original problem.

maxSubArray for array with n numbers:
* If n == 1 : return this single element.
* left_sum = maxSubArray for the left subarray, i.e. for the first n/2 numbers (middle element at index (left + right) / 2 always belongs to the left subarray).
* right_sum = maxSubArray for the right subarray, i.e. for the last n/2 numbers.
* cross_sum = maximum sum of the subarray containing elements from both left and right subarrays and hence crossing the middle element at index (left + right) / 2.
* Merge the subproblems solutions, i.e. return max(left_sum, right_sum, cross_sum).

2. Greedy
The algorithm is general and straightforward: iterate over the array and update at each step the standard set for such problems:
* current element
* current local maximum sum (at this given point)
* global maximum sum seen so far.

3. DP
There are two standard DP approaches suitable for arrays:
* Constant space one. Move along the array and modify the array itself.
* Linear space one. First move in the direction left->right, then in the direction right->left. Combine the results. Here is an example.

Let's use here the first approach since one could modify the array to track the current local maximum sum at this given point.
Next step is to update the global maximum sum, knowing the local one.
"""





# Greedy
# Time: O(N), where N is the length of nums
# Space: O(1)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        cur_max, max_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if cur_max > 0:
                cur_max += nums[i]
            else:
                if nums[i] >= cur_max:
                    cur_max = nums[i]
            if cur_max > max_sum:
                max_sum = cur_max
        return max_sum


# DP
# Time: O(N), >99%
# Space： O(1)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        # dp
        # nums[i] means cur_max_sum at point i
        for i in range(1, len(nums)):
            if nums[i-1] >= 0:
                nums[i] += nums[i-1]
            max_sum = max(max_sum, nums[i])
        return max_sum
            
            

# Divede and Conquer
# Time: O(NlogN), master theorem to solve the recurrence https://leetcode.com/problems/maximum-subarray/solution/
# Space: O(logN) to keep the recursion stack.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    
    def cross_sum(self, nums, left, right, p):
        """
        max_cross_sum = max_left_subsum + max_right_subsum
        calculate corss sum of subarray between left and right and corss the index p
        """
        if left == right:
            return nums[left]
        
        left_subsum = float('-inf')
        cur_sum = 0
        for i in range(p, left - 1, -1):
            cur_sum += nums[i]
            left_subsum = max(left_subsum, cur_sum)
        
        right_subsum = float('-inf')
        cur_sum = 0
        for i in range(p + 1, right + 1):
            cur_sum += nums[i]
            right_subsum = max(right_subsum, cur_sum)
        
        return left_subsum + right_subsum
    
    def helper(self, nums, left, right):
        """
        deal with the left subarray and right subarray
        return the max_sub_array between left index and right index of nums
        """
        # recursion terminator
        if left == right:
            return nums[left]
        
        p = (left + right ) // 2
        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p+1, right)
        cross_sum = self.cross_sum(nums, left, right, p)
        
        return max(left_sum, right_sum, cross_sum)
