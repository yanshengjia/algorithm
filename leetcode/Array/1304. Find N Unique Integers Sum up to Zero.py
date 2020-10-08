"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]


Solution:
use the numbers 1, 2, ..., n-1 as well as their negated sum
"""


# Time: O(1)
# Space: O(n)
class Solution:
    def sumZero(self, n: int) -> List[int]:
        l = list(range(1, n))
        neg_sum = -sum(l)
        return l + [neg_sum]
