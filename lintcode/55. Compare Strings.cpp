// Author: Shengjia Yan
// Date: 2017年8月3日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(m+n)  m与n分别是两个字符串的长度
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param A: A string includes Upper Case letters
     * @param B: A string includes Upper Case letter
     * @return:  if string A contains all of the characters in B return true 
     *           else return false
     */
    bool compareStrings(string A, string B) {
        // write your code here
        int array[128];
        memset(array, 0, sizeof(array));
        
        int la = A.length();
        int lb = B.length();
        
        for (int i=0; i<la; i++)
            array[A[i]]++;
        
        for (int j=0; j<lb; j++)
            array[B[j]]--;
            
        for (int k=0; k<128; k++) {
            if (array[k] < 0) {
                return false;
            }
        }
        
        return true;
    }
};
