"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


Solutions:
1. Backtrack / DFS
"""


# Backtrack
# Time: O(4^n/n^0.5) https://leetcode.com/problems/generate-parentheses/solution/
# Space: O(4^n/n^0.5)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(s = '', left = 0, right = 0):
            # left: number of left brackets we used
            # right: number of right brackets we used

            # stop condition
            if len(s) == n*2:
                res.append(s)
                return
            
            # make choice
            if left < n:
                backtrack(s + '(', left+1, right)
            if right < left:
                backtrack(s + ')', left, right+1)
        
        backtrack()
        return res
    

# DFS
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        left, right = n, n
        s = ''
        
        self.dfs(left, right, s)
        return self.res
    
    def dfs(self, left, right, s):
        # left: number of left brackets we have left to use
        # right: number of right brackets we have left to use
        if left == 0 and right == 0:
            self.res.append(s)
            return
        
        if left > 0:
            self.dfs(left-1, right, s+'(')
        if right > left:
            self.dfs(left, right-1, s+')')
