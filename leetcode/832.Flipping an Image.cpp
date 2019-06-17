// Author: Shengjia Yan
// Date: 2018-05-14 Monday
// Email: i@yanshengjia.com
// Time Complexity: O(mn)
// Space Complexity: O(1)

class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        int row = A.size();
        int col = A[0].size();
        
        for (int i=0; i<row; i++) {
            for (int j=0; j<(col/2); j++) {
                int t = A[i][j];
                A[i][j] = A[i][col-j-1];
                A[i][col-j-1] = t;
            }
        }
        
        for (int i=0; i<row; i++) {
            for (int j=0; j<col; j++) {
                A[i][j] = 1 - A[i][j];
            }
        }
        return A;
    }
};