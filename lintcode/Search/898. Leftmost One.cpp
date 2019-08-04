// Author: Shengjia Yan
// Date: 2018-04-10 Tuesday
// Email: i@yanshengjia.com
// Time Complexity: O(n^2)
// Space Complexity: O(1)

class Solution {
public:
    /**
     * @param arr: The 2-dimension array
     * @return: Return the column the leftmost one is located
     */
    int getColumn(vector<vector<int>> &arr) {
        // Write your code here
        int row = arr.size();
        int col = arr[0].size();
        
        for (int i=0; i<col; i++) {
            for (int j=0; j<row; j++) {
                if (arr[j][i]) {
                    return i;
                }
            }
        }
    }
};