// Author: Shengjia Yan
// Date: 2017年7月9日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(n)


class Solution {
public:
    /** 
     *@param A: A list of integers
     *@param elem: An integer
     *@return: The new length after remove
     */
    int removeElement(vector<int> &A, int elem) {
        // write your code here
        int new_length = 0;
        int size = A.size();
        vector<int> B;
        
        for (int i=0; i<size; i++) {
            if (A[i] != elem) {
                new_length++;
                B.push_back(A[i]);
            }
        }
        
        A.clear();
        A = B;
        return new_length;
    }
};