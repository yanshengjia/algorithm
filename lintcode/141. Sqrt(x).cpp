// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(logn)
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param x: An integer
     * @return: The sqrt of x
     */
    int sqrt(int x) {
        // write your code here
        long long int low = 0, high = x, mid;
        
        while(low <= high) {
            mid = (low + high) / 2;
            
            if (mid * mid == x) {
                return mid;
            }
            else if (mid * mid < x) {
                if ((mid + 1) * (mid + 1) > x) {
                    return mid;
                }
                
                low = mid + 1;
            }
            else {
                // mid*mid > x
                if ((mid - 1) * (mid - 1) <= x) {
                    return mid-1;
                }
                
                high = mid - 1;
            }
        }
        return -1;
    }
};