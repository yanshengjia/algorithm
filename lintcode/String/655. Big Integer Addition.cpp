// Author: Shengjia Yan
// Date: 2017年7月30日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(m+n) m与n分别为2个字符串的长度
// Space Complexity: O(m+n)


class Solution {
public:
    /**
     * @param num1 a non-negative integers
     * @param num2 a non-negative integers
     * @return return sum of num1 and num2
     */
    string addStrings(string& num1, string& num2) {
        // Write your code here
        int l1 = num1.length(), l2 = num2.length();
        
        if (l1 == 0)    return num2;
        if (l2 == 0)    return num1;
        
        int guard1 = l1 - 1, guard2 = l2 - 1;
        string res = "";
        stack<char> cache;
        int carry = 0;
        
        while (guard1 >= 0 && guard2 >= 0) {
            int n1 = num1[guard1] - 48;
            int n2 = num2[guard2] - 48;
            int sum = n1 + n2 + carry;
            
            if (sum >= 10) {
                carry = 1;
                sum %= 10;
            } else {
                carry = 0;
            }
            
            char a = char(sum+48);
            cache.push(a);
            
            guard1--;
            guard2--;
        }
        
        if (guard1 == -1) {
            while (guard2 >= 0) {
                int n2 = num2[guard2] - 48;
                int sum = n2 + carry;
                
                if (sum >= 10) {
                    carry = 1;
                    sum %= 10;
                } else {
                    carry = 0;
                }
                
                char a = char(sum+48);
                cache.push(a);
                
                guard2--;
            }
        }
        
        if (guard2 == -1) {
            while (guard1 >= 0) {
                int n1 = num1[guard1] - 48;
                int sum = n1 + carry;
                
                if (sum >= 10) {
                    carry = 1;
                    sum %= 10;
                } else {
                    carry = 0;
                }
                
                char a = char(sum+48);
                cache.push(a);
                
                guard1--;
            }
        }
        
        if (carry == 1) {
            cache.push('1');
        }
        
        while (!cache.empty()) {
            res += cache.top();
            cache.pop();
        }
        
        return res;
    }
};