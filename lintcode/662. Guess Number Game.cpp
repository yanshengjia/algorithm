// Author: Shengjia Yan
// Date: 2017年8月20日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(logN)    logN 是以2为底的
// Space Complexity: O(1)


// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    /**
     * @param n an integer
     * @return the number you guess
     */
    int guessNumber(int n) {
        // Write your code here
        long long int low = 1, high = n;
        
        while (low <= high) {
            long long int mid = (low + high) / 2;
            int t = guess(mid);
            
            if (t == 0) {
                return mid;
            }
            else if (t == 1) {
                low = mid + 1;
            }
            else {
                high = mid - 1;
            }
        }
    }
};