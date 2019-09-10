"""
Given a string S, return the number of substrings that have only one distinct letter.


Example 1:

Input: S = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.
Example 2:

Input: S = "aaaaaaaaaa"
Output: 55


Solution:
One Pass
a string with k consecutive chars has ```k*(k+1)/2``` combinations
"""


# One Pass
# Time: O(N), where N is the length of S
# Space: O(1)
class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """
        res = 0
        l = 0
        pre = 'A'
        for i in range(len(S)):
            s = S[i]
            if s != pre:
                res += l * (l+1) / 2
                pre = s
                l = 1
            else:
                l += 1
        res += l * (l+1) / 2    # deal with last sequence
        return res
