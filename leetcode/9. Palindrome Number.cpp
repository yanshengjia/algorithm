// Author: Shengjia Yan
// Date: 2018-04-25 Wednesday
// Email: i@yanshengjia.com
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0)
            return false;
        
        string str = to_string(x);  // C++ 11

        /* another way to convert number to str
        std::string s;
        std::stringstream out;
        out << x;
        s = out.str();
        */
        
        int l = str.size();
        
        for (int i=0; i<l/2; i++) {
            if (str[i] != str[l-i-1])
                return false;
        }
        return true;
    }
};