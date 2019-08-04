"""
Write an algorithm to determine if a number is happy.

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.


Example 1:

Input:19
Output:true
Explanation:

19 is a happy number

    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1


Solution:
Check if the number is repeated in the process of transformation, if yes, return false
"""


class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        # Write your code here
        d = {}
        while True:
            d[n] = 1
            n = sum([int(x) * int(x) for x in list(str(n))])
            if n == 1 or n in d:
                break
        return n == 1