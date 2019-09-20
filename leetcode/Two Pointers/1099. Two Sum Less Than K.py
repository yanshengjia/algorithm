"""
Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.


Solution:
Sort + Two Pointers
"""


# Two Pointers
# Time: O(NlogN + N) = O(NlogN), > 91%
# Space: O(1)
class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) < 2:
            return -1
        A.sort()
        if A[0] + A[1] >= K:
            return -1
        i, j = 0, len(A) - 1
        S = 0
        while i < j:
            t = A[i] + A[j]
            if t < K:
                if t > S:
                    S = t
                i += 1
            else:
                j -= 1
        return S
            