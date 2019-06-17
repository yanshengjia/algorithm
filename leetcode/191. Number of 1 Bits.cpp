// Author: Shengjia Yan
// Date: 2018-05-30 Wednesday
// Email: i@yanshengjia.com


// Time Complexity: O(logn)
// Space Complexity: O(1)
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int res = 0;
        while (n) {
            if (n % 2)  res++;
            n /= 2;
        }
        return res;
    }
};

// Time Complexity: O(1)
// Space Complexity: O(1)
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int res = 0;
        while (n) {
            if (n & 1)  res++;
            n >>= 1;
        }
        return res;
    }
};