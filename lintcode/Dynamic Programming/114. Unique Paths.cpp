// Author: Shengjia Yan
// Date: 2017年7月28日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n^2) DP
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param n, m: positive integer (1 <= n ,m <= 100)
     * @return an integer
     */
    int uniquePaths(int m, int n) {
        // wirte your code here
        int dp[100][100];
        
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (i*j == 0) {
                    dp[i][j] = 1;
                    continue;
                }

                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        
        return dp[m-1][n-1];
    }
};
