"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

Example 1:

Input: "())"
Output: 1
Example 2:

Input: "((("
Output: 3
Example 3:

Input: "()"
Output: 0
Example 4:

Input: "()))(("
Output: 4


Solution:
1. Stack
When we meet '(', push into stack.
When we meet ')', if the top of stack is '(', it's a match and we pop '('; otherwise push ')' into stack.

2. Balance
When we meet '(', balance - 1; When we meet ')', balance += 1
If balance < 0, increment res.
"""


# Stack
# Time: O(n)
# Space: O(n) at worst case
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for s in S:
            if s == '(':
                stack.append(s)
            else:   # )
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s)
        
        return len(stack)



# Balance
# Time: O(n)
# Space: O(1)
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        res, balance = 0, 0
        for s in S:
            if s == '(':
                balance +=1
            else:
                balance -= 1
            
            # balance >= -1
            if balance < 0:
                res += 1
                balance += 1
        
        return res + balance


