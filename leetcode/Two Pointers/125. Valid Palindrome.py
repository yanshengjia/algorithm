"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false


Solution:
1. preprocess the string, remove all extra chars
2. two pointers
"""


# two pointers
# Time-O(N), where N is the length of s
# Space-O(1)
def isPalindrome(self, s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        new_s = ''
        for c in s:
            if 48 <= ord(c) <= 57 or 97 <= ord(c) <= 122:
                new_s += c
        l = len(new_s)
        for i in range(l//2):
            if new_s[i] != new_s[l-i-1]:
                return False
        return True
        