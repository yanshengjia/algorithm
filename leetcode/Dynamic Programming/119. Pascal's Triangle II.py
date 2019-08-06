"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

Example:
Input: 3
Output: [1,3,3,1]

Follow up:
Could you optimize your algorithm to use only O(k) extra space?

Solution:
DP
dp[i][j] = dp[i-1][j-1] + dp[i-1][j], 0<j<len-1
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        dp = [[1]]
        for i in range(1, rowIndex+1):
            line = [1 for j in range(i+1)]
            for j in range(1, i):
                line[j] = dp[i-1][j-1] + dp[i-1][j]
            dp.append(line)
        return dp[rowIndex]
        