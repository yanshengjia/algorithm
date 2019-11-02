"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4


Solution:
2D DP
dp[r][c] represent the len of side of the max square whose bottom right corner is matrix[r][c]

if matrix[r][c] == '1':
	dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1]) + 1
"""


# Time: O(mn), where m, n are the side lengths of matrix
# Space: O(mn)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        
        max_len = 0
        for i in range(row):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0] == 1:
                max_len = 1
        for i in range(col):
            dp[0][i] = int(matrix[0][i])
            if dp[0][i] == 1:
                max_len = 1
        
        
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][c] == '1':
                    dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1]) + 1
                    if dp[r][c] > max_len:
                        max_len = dp[r][c]
        
        return max_len * max_len
