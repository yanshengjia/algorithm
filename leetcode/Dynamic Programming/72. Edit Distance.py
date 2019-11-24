"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Solution:
DP Formula:
* if i == 0 and j == 0, edit(i, j) = 0
* if i == 0 and j > 0, edit(i, j) = j
* if i > 0 and j == 0, edit(i, j) = i
* if i ≥ 1 and j ≥ 1, edit(i, j) == min( edit(i-1, j) + 1, edit(i, j-1) + 1, edit(i-1, j-1) + f(i, j) ), if word1[i] != word2[i], f(i, j) = 1; otherwise f(i, j) = 0

1. Recursion
2. Iteration
"""


# Recursion (TLE)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        return self.edit(word1, word2, l1, l2)
    
    def edit(self, str1: str, str2: str, i: int, j: int):
        # return the edit distance of str1[:i] and str2[:j]
        if i == 0 and j == 0:
            return 0
        elif i > 0 and j == 0:
            return i
        elif i == 0 and j > 0:
            return j
        else:
            up = self.edit(str1, str2, i-1, j) + 1
            left = self.edit(str1, str2, i, j-1) + 1
            left_up = self.edit(str1, str2, i-1, j-1)
            if str1[i-1] != str2[j-1]:
                left_up += 1
            min_distance = min(up, left, left_up)
            return min_distance


# Iteration
# Time: O(mn)
# Space: O(mn)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        
        # dp[i][j]: the edit distance of word1[:i] and word2[:j]
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
        
        # init
        for i in range(l1+1):
            dp[i][0] = i
        for i in range(l2+1):
            dp[0][i] = i
        
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                up = dp[i-1][j] + 1
                left = dp[i][j-1] + 1
                if word1[i-1] == word2[j-1]:
                    left_up = dp[i-1][j-1]
                else:
                    left_up = dp[i-1][j-1] + 1
                
                dp[i][j] = min(up, left, left_up)
        return dp[l1][l2]
        
        
