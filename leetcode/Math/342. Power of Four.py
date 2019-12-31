"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

Solution:
If num is a power of four x = 4^a, then a = log_4 x = 1/2 log_2 x is an integer. Hence let's simply check if log_2 x is an even number.
"""

from math import log2
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num > 0 and log2(num) % 2 == 0:
            return True
        else:
            return False
