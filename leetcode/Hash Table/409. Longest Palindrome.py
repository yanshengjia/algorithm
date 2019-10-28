"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.


Solution:
Count the characters. If the number of a char is even, they are all be a part of palindrome. If Odd, thay may all belong to the palindrome.
"""


# Time: O(n), where n is the length of s
# Space: O(1), since the alphabet size is limited
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        
        res = 0
        flag_mid = True
        for k, v in d.items():
            if v % 2:
                if flag_mid:
                    res += v
                    flag_mid = False
                else:
                    res += v - 1
            else:
                res += v
    
        return res
