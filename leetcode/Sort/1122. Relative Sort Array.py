"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

 
Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
 

Constraints:

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
Each arr2[i] is distinct.
Each arr2[i] is in arr1.


Solution:
1. Count + Dict
2. Counting Sort
"""


# Count + Dict
# Time: O(NlogN), N is the length of arr1
# Space: O(N)
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = dict()
        extra = []
        res = []
        for a in arr1:
            if a in arr2:
                d[a] = d.get(a, 0) + 1
            else:
                extra.append(a)
        
        for a in arr2:
            res.extend([a]*d[a])
        
        res.extend(sorted(extra))
        return res



# Counting Sort
# Time: O(N)
# Space: O(1)
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = [0 for _ in range(1001)]
        
        # count numbers in arr1
        for a in arr1:
            cnt[a] += 1
        
        # place numbers based on arr2 order
        # use arr1 as res list
        i = 0
        for a in arr2:
            while cnt[a] > 0:
                arr1[i] = a
                i += 1
                cnt[a] -= 1
        
        # place numbers which are not in arr2
        for j in range(1001):
            while cnt[j] > 0:
                arr1[i] = j
                i += 1
                cnt[j] -= 1
        
        return arr1
