// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param num a positive number
     * @return true if it's a palindrome or false
     */
    bool palindromeNumber(int num) {
        // Write your code here
        string p = to_string(num);
        int size = p.size();
        bool flag = true;
        
        for (int i=0; i<size/2; i++) {
            if (p[i] != p[size-i-1])
                flag = false;
        }
        
        return flag;
    }
};