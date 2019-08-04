// Author: Shengjia Yan
// Date: 2017年7月30日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(m+n) m与n分别是2个字符串的长度
// Space Complexity: O(m+n)


class Solution {
public:
    /**
     * @param a a number
     * @param b a number
     * @return the result
     */
    string addBinary(string& a, string& b) {
        // Write your code here
        int la = a.length(), lb = b.length();
        
        if (la == 0)    return b;
        if (lb == 0)    return a;
        
        int guard_a = la - 1, guard_b = lb - 1;
        string res = "";
        stack<char> cache;
        int carry = 0;
        
        while (guard_a >= 0 && guard_b >= 0) {
            int num_a = a[guard_a] - 48;
            int num_b = b[guard_b] - 48;
            int sum = num_a + num_b + carry;
            
            switch (sum) {
                case 0:
                    cache.push('0');
                    carry = 0;
                    break;
                case 1:
                    cache.push('1');
                    carry = 0;
                    break;
                case 2:
                    cache.push('0');
                    carry = 1;
                    break;
                case 3:
                    cache.push('1');
                    carry = 1;
                    break;
            }
            
            guard_a--;
            guard_b--;
        }
        
        if (guard_a == -1) {
            while (guard_b >= 0) {
                int num_b = b[guard_b] - 48;
                int sum = num_b + carry;
                
                switch (sum) {
                    case 0:
                        cache.push('0');
                        carry = 0;
                        break;
                    case 1:
                        cache.push('1');
                        carry = 0;
                        break;
                    case 2:
                        cache.push('0');
                        carry = 1;
                        break;
                    case 3:
                    cache.push('1');
                    carry = 1;
                    break;
                }
                
                guard_b--;
            }
        }
        
        if (guard_b == -1) {
            while (guard_a >= 0) {
                int num_a = a[guard_a] - 48;
                int sum = num_a + carry;
                
                switch (sum) {
                    case 0:
                        cache.push('0');
                        carry = 0;
                        break;
                    case 1:
                        cache.push('1');
                        carry = 0;
                        break;
                    case 2:
                        cache.push('0');
                        carry = 1;
                        break;
                    case 3:
                        cache.push('1');
                        carry = 1;
                        break;
                }
                
                guard_a--;
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