"""
The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.

Given a positive integer N, return true if and only if it is an Armstrong number.


Example 1:

Input: 153
Output: true
Explanation: 
153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.
Example 2:

Input: 123
Output: false
Explanation: 
123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.


Solution:
Find the least significant digit of a number by taking it modulus 10. 
Remove it by dividing the number by 10 (integer division).
Once you have a digit, you can raise it to the power of k and add it to the sum.
"""


# > 99.7%
# Time: O(k), where k is the length of N
# Space: O(1)
import math
class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        s = 0
        guard = N
        k = len(str(N))
        while N > 0:
            digit = N % 10
            s += math.pow(digit, k)
            N //= 10
        if s == guard:
            return True
        else:
            return False
        