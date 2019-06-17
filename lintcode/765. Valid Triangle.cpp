// Author: Shengjia Yan
// Date: 2018-04-08 Sunday
// Email: i@yanshengjia.com
// Time Complexity: O(1)
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param a: a integer represent the length of one edge
     * @param b: a integer represent the length of one edge
     * @param c: a integer represent the length of one edge
     * @return: whether three edges can form a triangle
     */
    bool isValidTriangle(int a, int b, int c) {
        // write your code here
        if (a + b > c && b + c > a && a + c > b)
            return true;
        else
            return false;
    }
};