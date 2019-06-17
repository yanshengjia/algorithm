// Author: Shengjia Yan
// Date: 2018-04-08 Sunday
// Email: i@yanshengjia.com
// Time Complexity: O(1)
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param number: A 3-digit number.
     * @return: Reversed number.
     */
    int reverseInteger(int number) {
        // write your code here
        int a, b, c;
        c = number % 10;
        b = (number / 10) % 10;
        a = number / 100;
        int reverse_number = c * 100 + b * 10 + a;
        return reverse_number;
    }
};