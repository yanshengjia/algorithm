// Author: Shengjia Yan
// Date: 2017年7月22日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(1)
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param num a non-negative integer
     * @return one digit
     */
    int addDigits(int num) {
        // Write your code here
        if (num == 0) return 0;
        if (num % 9 == 0) return 9;
        if (num % 9 != 0) return num % 9;
    }
};