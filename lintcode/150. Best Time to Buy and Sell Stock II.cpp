// Author: Shengjia Yan
// Date: 2017年7月20日
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
        
        if (size == 0 || size == 1) return 0;
        
        int minPrice = prices[0], profit = 0;
        
        for (int i=1; i<size; i++) {
            if (prices[i] > minPrice) {
                profit += prices[i] - minPrice;
                minPrice = prices[i];
            }
            else {
                minPrice = prices[i];   
            }
        }
        
        return profit;
    }
};