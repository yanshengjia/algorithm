"""
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.


Solution:
Use Hashtable to record the frequency of numbers, a number in intersection should have the frequency of 3
"""


# Time: O(m+n+q), m n q is the length of 3 arrays
# Space: O(x), x it the size of intersection
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        d = dict()
        for c in arr1:
            d[c] = d.get(c, 0) + 1
        for c in arr2:
            d[c] = d.get(c, 0) + 1
        for c in arr3:
            d[c] = d.get(c, 0) + 1
        
        res = []
        for k, v in d.items():
            if v == 3:
                res.append(k)
        res.sort()
        return res
        
        