"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


Solution:
DP
dp[i][j] = dp[i-1][j-1] + dp[i-1][j], 0<j<len-1
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        dp = [[1]]
        for i in range(1, numRows):
            line = [1 for j in range(i+1)]
            for j in range(1, i):
                line[j] = dp[i-1][j-1] + dp[i-1][j]
            dp.append(line)
        return dp
