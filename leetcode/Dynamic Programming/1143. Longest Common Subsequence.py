"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Solution:
2D DP
dp[i][j]: the length of LCS of str1[:i] and str2[:j]

dp[i][j] = 0, if i == 0 or j == 0
         = dp[i-1][j-1], if str1[i] == str2[j] and i > 0 and j > 0
		 = max(dp[i][j-1], dp[i-1][j]), if str[i] != str2[j] and i > 0 and j > 0
							
"""


# 2D DP
# Time: O(mn), m and n are the length of str1 and str2
# Space: O(mn)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        # dp[i][j]: the length of LCS of text1[:i] and text2[:j]
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[m][n]