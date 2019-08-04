// Author: Shengjia Yan
// Date: 2017年9月26日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(m+n)  m是字符串A的长度，n是字符串B的长度
// Space Complexity: O(1)


class Solution {
public:
    /*
     * @param A: a string
     * @param B: a string
     * @return: a boolean
     */
    bool Permutation(string &A, string &B) {
        // write your code here
        int array[128];
        memset(array, 0, sizeof(array));
        
        int size_a = A.size();
        int size_b = B.size();
        
        for (int i=0; i<size_a; i++) {
            array[A[i]]++;
        }
        
        for (int j=0; j<size_b; j++) {
            array[B[j]]--;
        }
        
        for (int i=0; i<128; i++) {
            if (array[i] != 0)  return false;
        }
        
        return true;
    }
};