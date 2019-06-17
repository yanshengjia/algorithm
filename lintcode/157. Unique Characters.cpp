// Author: Shengjia Yan
// Date: 2017年7月21日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)  n为字符串长度
// Space Complexity: O(1)

class Solution {
public:
    /**
     * @param str: a string
     * @return: a boolean
     */
    bool isUnique(string &str) {
        // write your code here
        int array[126];
        memset(array, 0, sizeof(array));
        int size = str.length();
        
        for (int i=0; i<size; i++) {
            array[str[i]]++;
            
            if (array[str[i]] > 1) {
                return false;
            }
        }
        
        return true;
    }
};