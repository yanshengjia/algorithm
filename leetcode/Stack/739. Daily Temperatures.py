"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].


Solution:
Stack, Store (index, value)
When meet the next greater element, pop the stack and update the res[idx]
Similiar to "Next Greater Element"
"""


# Stack
# Time: bigger than O(n), n is the list length
# Space: O(n) at worst case
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res, stack = [], []
        
        for i in range(len(T)):
            while stack and stack[-1][1] < T[i]:
                idx = stack.pop()[0]
                res[idx] = i - idx
            
            stack.append((len(res), T[i]))
            res.append(0)   # placeholder
        return res
