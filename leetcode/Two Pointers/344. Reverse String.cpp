// created by sjyan @2016-11-11
// Time Complexity: O(n)    Space Complexity: O(1)

class Solution {
public:
    string reverseString(string s) {
        int length = s.size();
        int iter = length/2;
        
        for(int i=0; i<iter; i++){
            char t = s[i];
            s[i] = s[length-1-i];
            s[length-1-i] = t;
        }
        
        return s;
    }
};