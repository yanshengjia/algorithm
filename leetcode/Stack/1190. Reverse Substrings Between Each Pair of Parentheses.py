"""
Given a string s that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any bracket.


Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Example 4:

Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"


Solution:
Use two stack, one for the result, one for the substring needed to be reversed
pop the substring from the innerest parentheses to outter recursively
"""


# stack
# Time: O(N), >100%, where N is the length of s
# Space: O(N), >100%
class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        reverse = []
        
        for i in range(len(s)):
            if s[i] == ')':  # pop the substring between nearest parentheses
                p = stack.pop()
                while p != '(':
                    reverse.append(p)
                    p = stack.pop()
                stack += reverse
                reverse = []
            else:
                stack.append(s[i])
        return ''.join(stack)
        