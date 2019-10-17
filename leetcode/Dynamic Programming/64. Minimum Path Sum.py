"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


Solution:
DP 2D
cost(i, j) = grid[i][j] + min(cost(i+1, j), cost(i, j+1))
"""


# Time: O(mn), we traverse the entire matrix once
# Space: O(mn), if we use the original grid matrix as our dp matrix, the Space complexity would be O(1)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        
        dp[0][0] = grid[0][0]
        # 1st row
        for i in range(1, col):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        
        # 1st col
        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
        return dp[-1][-1]
