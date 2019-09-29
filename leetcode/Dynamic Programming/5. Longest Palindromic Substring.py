"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"


Solution:
DP
define dp[i][j]: if substring s[i:j+1] is a palindrome
base case: one and two letters palindrome
P(i,j) = (P(i+1,j−1) and s[i] == s[j])
increment the substring len and find longest palindromic substring 
"""


# DP
# Time: O(N^2), where N is the length of s
# Space: O(N^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        dp = [[0 for _ in range(l)] for _ in range(l)]
        
        max_len = 0
        res = ""
        # base case
        # one letter palindromes
        for i in range(l):
            max_len = 1
            res = s[i]
            dp[i][i] = 1
        # two letters palindromes
        for i in range(l-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                max_len = 2
                res = s[i:i+2]
        
        # dp P(i,j) = (P(i+1,j−1) and s[i] == s[j])
        # increment the substring len and find longest palindromic substring 
        for gap in range(2, l):
            for i in range(l - gap):
                j = i + gap
                if s[i] == s[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1
                    if gap + 1 > max_len:
                        max_len = gap + 1
                        res = s[i:j+1]
        return res
