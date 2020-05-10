"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


Solution:
Two Pointers.
We can use the standard two-pointer approach that starts at the left and right of the string and move inwards. 
Whenever there is a mismatch, we can either exclude the character at the left or the right pointer.
We then take the two remaining substrings and compare against its reversed and see if either one is a palindrome.
"""


# Two Pointers
# Time: O(n), n is the length of s
# Space: O(n)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                s1 = s[l:r]
                s2 = s[l+1:r+1]
                return s1 == s1[::-1] or s2 == s2[::-1]
        return True