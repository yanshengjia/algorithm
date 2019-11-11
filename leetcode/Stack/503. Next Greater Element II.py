"""
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.


Solution:
Stack
Need to search circularly, we can enlarge the nums by twice or enlarge the loop range of i by twice.
"""


# Time: O(n), actually 2n
# Space: O(n)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        l = len(nums)
        nums = nums + nums
        stack, res = [], []
        
        for i in range(len(nums)):
            while stack and stack[-1][1] < nums[i]:
                idx = stack.pop()[0]
                res[idx] = nums[i]
            
            stack.append((len(res), nums[i]))
            res.append(-1)
        return res[:l]
        
        
        