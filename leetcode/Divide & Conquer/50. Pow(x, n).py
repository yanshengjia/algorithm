"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Solution:
Divide and Conquer, Divide n by 2 repeatedly
1. Recursion
2. Iteration    https://leetcode.com/problems/powx-n/solution/
"""


# Recursion
# Time: O(logn)
# Space: O(logn), recursion call stack
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        if n % 2:   # n is odd
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n//2)


# Iteration
# Try to understand the odd n case as we will lose some x in product, so we need to multiple it to the res
# Time: O(logn)
# Space: O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
    
        if n < 0:
            n *= -1
            x = 1 / x
        
        res = 1
        product = x
        while n > 0:
            if n % 2 == 1:
                res *= product
            product = product * product
            n //= 2
        return res
