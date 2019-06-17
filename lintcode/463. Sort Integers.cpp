// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n^2)
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param A an integer array
     * @return void
     */
    void sortIntegers(vector<int>& A) {
        // Write your code here
        int size = A.size();
        
        for (int i=0; i<size-1; i++) {
            for (int j=0; j<size-i-1; j++) {
                int temp;
                if (A[j] > A[j+1]) {
                    temp = A[j+1];
                    A[j+1] = A[j];
                    A[j] = temp;
                }
            }
        }
    }
};