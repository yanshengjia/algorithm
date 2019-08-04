// Author: Shengjia Yan
// Date: 2017年7月22日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(1)
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param n The integer
     * @return Roman representation
     */
    string intToRoman(int n) {
        // Write your code here
        int num[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string str[] = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };
        string res = "";
        int i = 0;
        
        while (n > 0) {
            if (n >= num[i]) {
                res += str[i];
                n -= num[i];
            } else {
                i++;
            }
        }
        
        return res;
    }
};