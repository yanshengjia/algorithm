"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5


Solution:
* strip and split
* pointer
"""


# strip and split
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s.strip()) == 0:
            return 0
        last_word = s[::-1].split()[0]
        return len(last_word)


# pointer (faster)
# time-O(n)
# space-O(1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i].isspace():
            i -= 1
        res = 0
        while i >= 0 and not s[i].isspace():
            res += 1
            i -= 1
        return res

