"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).


Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


Solution:
1. Recursion
2. Non-Recursive Iterative While-loop
"""


# Recursion
# Time: O(N) > 15%
# Space: O(N)
class Solution:
    def fib(self, N: int) -> int:
        if N in [0, 1]:
            return N
        return self.fib(N-1) + self.fib(N-2)


# Iterative
# Time: O(N) > 70%
# Space: O(1)
class Solution:
    def fib(self, N: int) -> int:
        if N in [0, 1]:
            return N
        pre, cur = 0, 1
        while N > 1:
            res = pre + cur
            pre = cur
            cur = res
            N -= 1
        return res