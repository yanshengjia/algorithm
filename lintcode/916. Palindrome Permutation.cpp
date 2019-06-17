// Author: Shengjia Yan
// Date: 2018-04-10 Tuesday
// Email: i@yanshengjia.com
// Time Complexity: O(n)  n: length of string s
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param s: the given string
     * @return: if a permutation of the string could form a palindrome
     */
    bool canPermutePalindrome(string &s) {
        // write your code here
        int ascii[122];
        memset(ascii, 0, sizeof(ascii));
        
        int l = s.length();
        for (int i=0; i<l; i++) {
            ascii[s[i]]++;
        }
        
        int odd_counter = 0;
        for (int j=65; j<123; j++) {
            if (ascii[j] % 2) {
                odd_counter++;
                if (odd_counter > 1)
                    return false;
            }
        }
        return true;
    }
};