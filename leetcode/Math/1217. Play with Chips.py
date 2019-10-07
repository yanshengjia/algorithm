"""
There are some chips, and the i-th chip is at position chips[i].

You can perform any of the two following types of moves any number of times (possibly zero) on any chip:

Move the i-th chip by 2 units to the left or to the right with a cost of 0.
Move the i-th chip by 1 unit to the left or to the right with a cost of 1.
There can be two or more chips at the same position initially.

Return the minimum cost needed to move all the chips to the same position (any position).


Example 1:

Input: chips = [1,2,3]
Output: 1
Explanation: Second chip will be moved to positon 3 with cost 1. First chip will be moved to position 3 with cost 0. Total cost is 1.
Example 2:

Input: chips = [2,2,2,3,3]
Output: 2
Explanation: Both fourth and fifth chip will be moved to position two with cost 1. Total minimum cost will be 2.


Solution:
Since the first move is free, we can combine all chips with even index together and all chips with odd index together.
The result is min(odd_count, even_count)
"""

# Time: O(N), N is the length of chips
# Space: O(1)
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odd_count = 0
        even_count = 0
        for c in chips:
            if c % 2:
                odd_count += 1
            else:
                even_count += 1
        
        if odd_count == 0 or even_count == 0:
            return 0
        cost = min(odd_count, even_count)
        return cost
