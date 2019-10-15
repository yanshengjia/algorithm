"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.


Solution:
二维dp
dp[i][j] 代表刷到第 i 个房子用颜色 j 的最小 cost

basic idea: 如果第i房子刷 color 0, 那么第i个房子刷墙的最小费用 = Min(第i-1房子刷 color1, 第i-1房子刷 color2) + costs[i][0]
go through all the houses, update dp[i][0], dp[i][1], dp[i][2] n-1 times
return the min one of three costs that last house painted with three colors.
"""


# DP
# Time: O(N), where N is the number of houses
# Space: O(N*3) since we allocate a new dp matrix. Can be O(1) if we use costs as our dp matrix.
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0 or len(costs[0]) == 0:
            return 0
        dp = costs
        for i in range(1, len(costs)):
            dp[i][0] += min(dp[i-1][1], dp[i-1][2])
            dp[i][1] += min(dp[i-1][0], dp[i-1][2])
            dp[i][2] += min(dp[i-1][1], dp[i-1][0])
        return min(dp[len(costs)-1][0], dp[len(costs)-1][1], dp[len(costs)-1][2])