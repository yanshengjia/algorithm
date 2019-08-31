"""
Given an array A of positive integers, let S be the sum of the digits of the minimal element of A.
Return 0 if S is odd, otherwise return 1.

Example 1:

Input: [34,23,1,24,75,33,54,8]
Output: 0
Explanation: 
The minimal element is 1, and the sum of those digits is S = 1 which is odd, so the answer is 0.
Example 2:

Input: [99,77,33,66,55]
Output: 1
Explanation: 
The minimal element is 33, and the sum of those digits is S = 3 + 3 = 6 which is even, so the answer is 1.


Solution:
Firstly we find the minimun number of array A.
Then we divide the number consecutively and get their remainder modulus 10.
Sum those remainders and return the answer as the problem asks.
"""


# Time: O(M + logN), where M is the length of array A, N is the minimun
# Space: O(1)
class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        m = float('inf')
        for a in A:
            if a < m:
                m = a
        
        s = 0
        while m > 0:
            s += m % 10
            m //= 10
        return 1 if s % 2 == 0 else 0
        