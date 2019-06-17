// Author: Shengjia Yan
// Date: 2018-04-10 Tuesday
// Email: i@yanshengjia.com
// Time Complexity: O(logn)
// Space Complexity: O(1)

class Solution {
public:
    /**
     * @param n: the number n 
     * @return: the times n convert to 1
     */
    int digitConvert(int n) {
        // Write your code here 
        int count = 0;
        
        while (n != 1) {
            if (n % 2) {
                n = 3 * n + 1;
            } else {
                n /= 2;
            }
            count++;
        }
        
        return count;
    }
};