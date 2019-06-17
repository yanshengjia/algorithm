// Author: Shengjia Yan
// Date: 2018-04-10 Tuesday
// Email: i@yanshengjia.com
// Time Complexity: O(1)
// Space Complexity: O(1)

class Solution {
public:
    /**
     * @param n: a number represent year
     * @return: whether year n is a leap year.
     */
    bool isLeapYear(int n) {
        // write your code here
        if (n % 400 == 0)
            return true;
        
        if (n % 4 == 0 && n % 100 != 0)
            return true;

        return false;
    }
};