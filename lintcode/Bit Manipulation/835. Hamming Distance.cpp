// Author: Shengjia Yan
// Date: 2018-04-10 Tuesday
// Email: i@yanshengjia.com
// Time Complexity: O(logn) n: x ^ y
// Space Complexity: O(1)

class Solution {
public:
    /**
     * @param x: an integer
     * @param y: an integer
     * @return: return an integer, denote the Hamming Distance between two integers
     */
    int hammingDistance(int x, int y) {
        // write your code here
        int z = x ^ y;
        int res = 0;
        while (z != 0) {
            if (z % 2) {
                res++;
            }
            z /= 2;
        }
        return res;
    }
};