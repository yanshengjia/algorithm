// Author: Shengjia Yan
// Date: 2017年7月24日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n) n为num的二进制表示中1的个数
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param num: an integer
     * @return: an integer, the number of ones in num
     */
    int countOnes(int num) {
        // write your code here
        int c = 0;
        for (c=0; num; c++) {
            num &= (num - 1);
        }
        return c;
    }
};