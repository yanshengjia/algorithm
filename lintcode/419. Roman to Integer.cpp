// Author: Shengjia Yan
// Date: 2017年7月22日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param s Roman representation
     * @return an integer
     */
    int romanToInt(string& s) {
        // Write your code here
        int res = 0;
        map<char, int> roman = {
                {'I', 1},
                {'V', 5},
                {'X', 10},
                {'L', 50},
                {'C', 100},
                {'D', 500},
                {'M', 1000}
        };
        
        int length = s.length();
        for (int i=0; i<length; i++) {
            if (i == length - 1 || roman[s[i]] >= roman[s[i+1]]) {
                res += roman[s[i]];
            } else {
                res -= roman[s[i]];
            }
        }
        
        return res;
    }
};