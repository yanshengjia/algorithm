// Author: Shengjia Yan
// Date: 2018-05-30 Wednesday
// Email: i@yanshengjia.com
// Time Complexity: O(n)
// Space Complexity: O(1)


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int size = prices.size();
        if (size == 0)  return 0;
        
        int min = prices[0];
        int max_profit = 0;
        
        for (int i = 0; i < size; i++) {
            if (prices[i] < min) {
                min = prices[i];
            }
            int temp = prices[i] - min;
            if (temp > max_profit) {
                max_profit = temp;
            }
        }
        return max_profit;
    }
};