"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5


Solution:
1. Hashtable, count frequency
2. Math trick. Exist a subarray of 4, majority number at least appear twice.
"""


# Hashtable
# Time: O(N), where N is the length of A
# Space: O(N)
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = set()
        for a in A:
            if a in s:
                return a
            s.add(a)


# compare elements with their neighbors that are distance 1, 2, or 3 away
# > 80%
# Time: O(N), where N is the length of A
# Space: O(1)
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for d in range(1, 4):
            for i in range(len(A) - d):
                if A[i] == A[i+d]:
                    return A[i]