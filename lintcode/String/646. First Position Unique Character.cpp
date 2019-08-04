// Author: Shengjia Yan
// Date: 2017年8月3日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(2n)  n为字符串长度
// Space Complexity: O(1)
// 扫两边字符串


class Solution {
public:
    /**
     * @param s a string
     * @return it's index
     */
    int firstUniqChar(string& s) {
        // Write your code here
        int l = s.length();
        
        if (l == 0) return -1;
        
        int array[128];
        memset(array, 0, sizeof(array));
        int repeat = 0;
        
        for (int i=0; i<l; i++)
            array[s[i]]++;
        
        for (int i=0; i<l; i++) {
            if (array[s[i]] == 1) {
                return i;
            }
        }
        
        return -1;
    }
};