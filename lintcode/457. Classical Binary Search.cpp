// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(logn)
// Space Complexity: O(1)
// 经典二分查找问题


class Solution {
public:
    /**
     * @param A an integer array sorted in ascending order
     * @param target an integer
     * @return an integer
     */
    int findPosition(vector<int>& A, int target) {
        // Write your code here
        int size = A.size();
        int low = 0, high = size-1, mid = 0;
        
        while (low <= high) {
            mid = (low + high) / 2;
            
            if (target == A[mid]) {
                return mid;
            }
            else if (target > A[mid]){
                low = mid + 1;
            }
            else {
                high = mid -1;
            }
        }
        
        return -1;
    }
};