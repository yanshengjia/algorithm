// Author: Shengjia Yan
// Date: 2018-05-29 Tuesday
// Email: i@yanshengjia.com
// Time Complexity: O(n)  n == length of s
// Space Complexity: O(1)


class Solution {
public:
    int titleToNumber(string s) {
        int length = s.size();
        int res = 0;
        
        for (int i=length-1; i>=0; i--) {
            int exp = length - i - 1;
            res += pow(26, exp) * (s[i] - 64);
        }

        return res;
    }
};