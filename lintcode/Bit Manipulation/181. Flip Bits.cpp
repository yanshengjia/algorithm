// Author: Shengjia Yan
// Date: 2017年7月24日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n) n为a与b两数不同位的个数
// Space Complexity: O(1)


class Solution {
public:
    /**
     *@param a, b: Two integer
     *return: An integer
     */
    int bitSwapRequired(int a, int b) {
        // write your code here
        int n = a ^ b;
        int c = 0;
        
        for (c=0; n; c++) {
            n &= (n-1);
        }
        
        return c;
    }
};