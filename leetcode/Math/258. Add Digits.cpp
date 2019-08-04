// Author: Shengjia Yan
// Date: 2018-05-29 Tuesday
// Email: i@yanshengjia.com
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
public:
    int addDigits(int num) {
        while (num / 10) {
            int sum = 0;
            while (num) {
                sum += num % 10;
                num /= 10;
            }
            num = sum;
        }
        return num;
    }
};

// Time Complexity: O(1)
class Solution {
public:
    int addDigits(int num) {
        return (num-1) % 9 + 1;
    }
};