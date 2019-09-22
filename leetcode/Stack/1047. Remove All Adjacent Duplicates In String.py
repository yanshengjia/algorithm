"""
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.


Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".


Solution:
1. Recursion  TLE
2. Replace
3. Stack *
"""


# Recursion
# Too slow
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        self.l = list(S)
        self.recursion()
        return ''.join(self.l)
    
    def recursion(self):
        flag = False
        i = 0
        while i < len(self.l) - 1:
            if self.l[i] == self.l[i+1]:
                flag = True
                break
            i += 1
        if flag:
            self.l = self.l[:i] + self.l[i+2:]
            self.recursion()


# Stack
# Time: O(N), > 80%, where N is the length of S
# Space: O(N) at worst case; O(N-D), D is a total length of all duplicates
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for c in S:
            if len(stack) == 0:
                stack.append(c)
            else:
                if c == stack[-1]:
                    stack.pop()
                else:
                    stack.append(c)
        return ''.join(stack)


# Replace duplicates
# Time complexity : {O}(N^2), where N is a string length. Here we have an onion : while -> for -> replace. while is executed not more then N/2 times, for is always run 26 times, and replace has O(N) run time in average. In total that results in O(N/2 xN×26×N) = O(N^2)
# Space complexity : O(N). The hashset of duplicates has the constant length 26, but replace function actually creates a copy of the string and thus uses O(N) space.
from string import ascii_lowercase
class Solution:
    def removeDuplicates(self, S: str) -> str:
        # generate 26 possible duplicates
        duplicates = {2 * ch for ch in ascii_lowercase}
        
        prev_length = -1
        while prev_length != len(S):
            prev_length = len(S)
            for d in duplicates:
                S = S.replace(d, '')
                
        return S
