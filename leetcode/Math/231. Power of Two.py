"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false


Solution:
1. While loop and Divide by 2
2. Bit Manipulation
a power of two in binary representation is one 1-bit, followed by some zeros

The problem will be solved in O(1) time with the help of bitwise operators. 
The idea is to discuss such bitwise (按位操作) tricks as
* How to get / isolate the rightmost 1-bit : x & (-x). keep the rightmost 1-bit and to set all the other bits to 0.
* How to turn off (= set to 0) the rightmost 1-bit : x & (x - 1).

These tricks are often used as something obvious in more complex bit-manipulation solutions, like for N Queens problem, and it's important to recognize them to understand what is going on.
"""


# While loop + Divide by 2
# Time: O(logN)
# Space: O(1)
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1 and n % 2 == 0:
            n //= 2
        return n == 1


# Bitwise Operators : Get the Rightmost 1-bit
# x & (-x)  keep the rightmost 1-bit and to set all the other bits to 0.
# Time: O(1), > 82%
# Space: O(1)
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        return (n & -n) == n


# Bitwise Operators : Turn off the Rightmost 1-bit
# x & (x-1)  set the rightmost 1-bit to zero.
# Time: O(1), > 99%
# Space: O(1)
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        return (n & n-1) == 0
        