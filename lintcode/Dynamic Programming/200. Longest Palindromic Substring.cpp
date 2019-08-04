// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n^2)
// Space Complexity: O(1)

class Solution {
public:
    /**
     * @param s input string
     * @return the longest palindromic substring
     */
    string longestPalindrome(string& s) {
        // Write your code here
        int size = s.size();
        
        if (size == 1) {
            return s;
        }
        
        int begin = 0;
        int maxlength = 1;
        int dp[1005][1005]; 
        memset(dp, 0, sizeof(dp));
        
        for (int i=0; i<size; i++) {
            dp[i][i] = 1;
            
            if (i<size-1 && s[i]==s[i+1]) {
                dp[i][i+1] = 1;
                begin = i;
                maxlength = 2;
            }
        }
        
        for (int l=3; l<=size; l++) {
            for (int i=0; i<=size-l; i++) {
                int j = i+l-1;  // substr end positon
                
                if (dp[i+1][j-1] && s[i]==s[j]) {
                    dp[i][j] = 1;
                    begin = i;
                    maxlength = l;
                }
            }
        }

        string maxsubstr = s.substr(begin, maxlength);
        return maxsubstr;
    }
};