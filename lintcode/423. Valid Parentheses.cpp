// Author: Shengjia Yan
// Date: 2017年8月9日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)    n为字符串长度
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param s A string
     * @return whether the string is a valid parentheses
     */
    bool isLeft(char c) {
    if (c == '{' || c == '[' || c == '(')
        return true;
    else 
        return false;
    }

    bool isMatch(char left, char right) {
        if (right == '}') {
            if (left == '{')
                return true;
            else
                return false; 
        }
        
        if (right == ']') {
            if (left == '[')
                return true;
            else
                return false; 
        }
    
        if (right == ')') {
            if (left == '(')
                return true;
            else
                return false; 
        }
    }
    
    bool isValidParentheses(string& s) {
        // Write your code here
        int size = s.length();
        if (size == 0)    return true;
    
        stack<char> cache;
        
        for (int i=0; i<size; i++) {
            if (isLeft(s[i])) {
                cache.push(s[i]);
            }
            else {
                if (cache.empty() || !isMatch(cache.top(), s[i])) {
                    return false;
                }
                
                cache.pop();
            } 
        }
    
        if (!cache.empty()) {
            return false;
        }
        
        return true;
    }
};