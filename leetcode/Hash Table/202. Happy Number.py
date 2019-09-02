"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1


Solution:
Calculate the sum of squares of digits od the number and store the sum in a set repeatedly. When the sum is 1, jump out of the while loop.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        d = set()
        while n != 1:
            new_n = self.calSquares(n)
            if new_n in d:
                return False
            else:
                d.add(new_n)
                n = new_n
            n = new_n    
        return True
    
    def calSquares(self, n):
        res = 0
        while n != 0:
            res += (n % 10) **2
            n //= 10
        return res
