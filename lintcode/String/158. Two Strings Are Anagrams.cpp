// Author: Shengjia Yan
// Date: 2017年7月24日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param s: The first string
     * @param b: The second string
     * @return true or false
     */
    bool anagram(string s, string t) {
        // write your code here
        int length_s = s.length();
        int length_t = t.length();
        int ascii[130];
        memset(ascii, 0, sizeof(ascii));
        
        for (int i=0; i<length_s; i++)
            ascii[s[i]]++;
        
        for (int j=0; j<length_t; j++)
            ascii[t[j]]--;
        
        for (int k=0; k<130; k++) {
            if (ascii[k] != 0)  return false;
        }
        return true;
    }
};