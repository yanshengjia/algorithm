"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


Solution:
Sieve of Eratosthenes https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
打表，2的倍数，3的倍数，5的倍数...
"""


# Time-O(n log log n)
# Space-O(n)
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        is_prime = [True] * n
        
        for i in range(2, int(n**0.5)+1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
        
        res = 0
        for i in range(2, n):
            if is_prime[i] == True:
                res += 1
        return res
        