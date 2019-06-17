// Author: Shengjia Yan
// Date: 2017年7月19日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n.length())
// Space Complexity: O(n.length())  这里的 n 指的是函数的参数 n

class Solution {
public:
    /**
     * @param n the integer to be reversed
     * @return the reversed integer
     */
    int reverseInteger(int n) {
        // Write your code here
        bool flagPositive = true;
        long long int r;
        int res;
        stringstream ss;
        string str;
        
        ss << n;
        str = ss.str();
        
        if (n < 0) {
            flagPositive = false;
            str = str.substr(1, str.length());
        }
        
        int size = str.length();
        
        for (int i=0; i<size/2; i++) {
            char temp = str[size-i-1];
            str[size-i-1] = str[i];
            str[i] = temp;
        }
        
        stringstream sss(str);  
        sss >> r;
        
        if (r > 2147483647) {
            return 0;
        }
        else {
            if (!flagPositive) {
                res = r * -1;
            }
            else {
                res = r;
            }
        }
        
        return res;
    }
};
