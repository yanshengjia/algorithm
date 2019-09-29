"""
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true


Solution:
Use a hashtable to store the frequency of nums
Trivial
"""


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = dict()
        for a in arr:
            d[a] = d.get(a, 0) + 1
        
        s = set()
        for k, v in d.items():
            if v not in s:
                s.add(v)
            else:
                return False
        return True
        