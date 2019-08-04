// Author: Shengjia Yan
// Date: 2017年8月4日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(m+n)  m与n分别是二维矩阵的长和宽
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param matrix: A list of lists of integers
     * @param target: An integer you want to search in matrix
     * @return: An integer indicate the total occurrence of target in the given matrix
     */
    int searchMatrix(vector<vector<int> > &matrix, int target) {
        // write your code here
        if (matrix.empty())
            return 0;
            
        int row = matrix.size(), col = matrix[0].size();
        int i = 0, j = col - 1, count = 0;
        
        while (i < row && j >= 0) {
            if (matrix[i][j] == target) {
                count++;
                i++;
            }
            else if (matrix[i][j] < target) {
                i++;
            }
            else {
                j--;
            }
        }
        
        return count;
    }
};
