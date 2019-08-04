// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param n: An integer
     * @return: An integer
     */
    int climbStairs(int n) {
        // write your code here
        long long int result = 1;
        long long int pre = 0;
        long long int next = 1;
        
        if (n == 0)
            return 1;
        else if (n == 1)
            return 1;
        else {
            while(n > 1) {
                n--;
                pre = next;
                next = result;
                result = pre + next;
            }
            return result;
        }
    }
};
