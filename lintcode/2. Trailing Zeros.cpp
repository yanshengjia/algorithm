// Author: Shengjia Yan
// Date: 2017年7月21日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(logn)
// Space Complexity: O(1)


class Solution {
 public:
    // param n : description of n
    // return: description of return 
    long long trailingZeros(long long n) {
        long long count5 = 0;
        
        while (n > 0) {
            count5 += (n / 5);
            n /= 5;
        }
        return count5;
    }
};
