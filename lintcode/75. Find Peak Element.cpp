// Author: Shengjia Yan
// Date: 2017年7月19日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
public:
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    int findPeak(vector<int> A) {
        // write your code here
        int n = A.size();
        
        if (A[1] > A[2]) return 1;
        if (A[n-2] > A[n-3]) return n-2;
        
        for (int i=2; i<n-2; i++) {
            if (A[i] > A[i-1] && A[i] > A[i+1]) {
                return i;
            }
        }
    }
};