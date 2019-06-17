// Author: Shengjia Yan
// Date: 2017年8月20日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(?)    undetermined
// Space Complexity: O(1)


class Solution {
public:
    /*
     * @param n: An integer
     * @return: true if this is a happy number or false
     */
    int transform(int n) {
        int sum = 0;
        while (n != 0) {
            sum += (n % 10) * (n % 10);
            n /= 10;
        }
        return sum;
    }
    
    
    bool isHappy(int n) {
        // write your code here
        if (n <= 0)    return false;
        
        while (n != 1) {
            n = transform(n);
            if (n == 4)    return false;
        }
        return true;
    }
};