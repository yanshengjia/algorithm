// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    int maxProfit(vector<int> &prices) {
        // write your code here
        int size = prices.size();
        int maxprofit = 0;
        int lowest = 0;
        
        if (size < 2) {
            return maxprofit;
        }
        
        lowest = prices[0];
        
        for (int i=1; i<size; i++) {
            maxprofit = max(maxprofit, prices[i] - lowest);
            lowest = min(lowest, prices[i]);
        }
        
        return maxprofit;
    }
};
