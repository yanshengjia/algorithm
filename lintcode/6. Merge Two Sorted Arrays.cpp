// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(m+n)
// Space Complexity: O(m+n)


class Solution {
public:
    /**
     * @param A and B: sorted integer array A and B.
     * @return: A new sorted integer array
     */
    vector<int> mergeSortedArray(vector<int> &A, vector<int> &B) {
        // write your code here
        if (A.empty()) {
            return B;
        }
        else if (B.empty()) {
            return A;
        }
        
        vector<int> result;
        
        int sizeA = A.size();
        int sizeB = B.size();
        int a = 0, b = 0;
        
        while (a<sizeA && b<sizeB) {
            if (A[a] < B[b]) {
                result.push_back(A[a]);
                a++;
            }
            else {
                result.push_back(B[b]);
                b++;
            }
        }
        
        if (a == sizeA) {
            while (b<sizeB) {
                result.push_back(B[b]);
                b++;
            }
        }
        
        if (b == sizeB) {
            while (a<sizeA) {
                result.push_back(A[a]);
                a++;
            }
        }
        
        return result;
    }
};