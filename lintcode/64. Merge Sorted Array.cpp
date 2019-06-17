// Author: Shengjia Yan
// Date: 2017年7月9日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(m+n)
// Space Complexity: O(m+n)


class Solution {
public:
    /**
     * @param A: sorted integer array A which has m elements, 
     *           but size of A is m+n
     * @param B: sorted integer array B which has n elements
     * @return: void
     */
    void mergeSortedArray(int A[], int m, int B[], int n) {
        // write your code here
        vector<int> res;
        int itra = 0, itrb = 0;
        
        while (itra < m && itrb < n) {
            if (A[itra] < B[itrb]) {
                res.push_back(A[itra]);
                itra++;
            }
            else {
                res.push_back(B[itrb]);
                itrb++;
            }
        }
        
        while (itra < m) {
            res.push_back(A[itra]);
            itra++;
        }
        
        while (itrb < n) {
            res.push_back(B[itrb]);
            itrb++;
        }
        
        for (int i=0; i<m+n; i++) {
            A[i] = res[i];
        }
    }
};