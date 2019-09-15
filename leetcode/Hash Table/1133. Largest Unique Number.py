"""
Given an array of integers A, return the largest integer that only occurs once.

If no integer occurs once, return -1.

Example 1:

Input: [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: 
The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.
Example 2:

Input: [9,9,8,8]
Output: -1
Explanation: 
There is no number that occurs only once.


Solution:
Hash table.
First find all unique numbers, and then pick the max.
"""

# Hash Table
# Time: O(N), where N is the length of A
# Space: O(N), since we keep up to the whole list A
class Solution(object):
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        d = dict()
        for a in A:
            d[a] = d.get(a, 0) + 1
        
        candidates = []
        for k, v in d.items():
            if v == 1:
                candidates.append(k)
        
        if len(candidates) == 0:
            return -1
        else:
            return max(candidates)