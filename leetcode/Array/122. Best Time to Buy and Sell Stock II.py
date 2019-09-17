"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


Solution:
1. Peak Valley Approach
TotalProfit = Sum(height(peak_i) - height(valley_i))
2. One Pass
we can simply go on crawling over the slope and keep on adding the profit obtained from every consecutive transaction
"""


# Peak Valley
# Time: O(N), >99%, where N is the length of prices
# Space: O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        res = 0
        min_p = prices[0]
        for i in range(1, len(prices)):
            if prices[i] <= min_p:
                min_p = prices[i]
            else:
                if i < len(prices) - 1:
                    if prices[i] <= prices[i+1]:
                        continue
                    else:
                        res += prices[i] - min_p
                        i += 1
                        min_p = prices[i]
                else:
                    if prices[i] > min_p:
                        res += prices[i] - min_p
        return res


# Peak Valley
# Time: O(N), > 100%
# Space: O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l == 0:
            return 0
        res = 0
        valley, peak = prices[0], prices[0]
        i = 0
        while i < l - 1:
            while i < l - 1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            while i < l - 1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            res += peak - valley
        return res
            

# One Pass
# Time: O(N)
# Space: O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res
