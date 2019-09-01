"""
Given an array A of distinct integers sorted in ascending order, return the smallest index i that satisfies A[i] == i.  Return -1 if no such i exists.


Example 1:

Input: [-10,-5,0,3,7]
Output: 3
Explanation: 
For the given array, A[0] = -10, A[1] = -5, A[2] = 0, A[3] = 3, thus the output is 3.
Example 2:

Input: [0,2,5,8,17]
Output: 0
Explanation: 
A[0] = 0, thus the output is 0.
Example 3:

Input: [-10,-5,3,4,7,9]
Output: -1
Explanation: 
There is no such i that A[i] = i, thus the output is -1.


Solution:
1. Linear Search
2. Binary Search
A[i] is distinct and ascending.
A[i] - i is non-descending array.
Binary search the first 0 in the array of A[i] - i.
"""


# Linear Search
# Time: O(N), where N is the length of A
# Space: O(1)
class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for i in range(len(A)):
            if A[i] == i:
                return i
        return -1



# Binary Search
# > 20%
# Time: O(logN), where N is the length of arrya A
# Space: O(1)
class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        # A[i] - i is a non-desending array
        i, j = 0, len(A)-1
        while i < j:
            mid = (i + j) // 2
            if i == mid and A[i] - i != 0:
                break
        
            if A[mid] - mid < 0:
                i = mid
            elif A[mid] - mid > 0:
                j = mid
            else:
                if mid == 0:
                    return mid
                else:
                    if A[mid-1] < mid -1:
                        return mid
                    else:
                        j = mid
        return -1


# Binary Search
# > 62%
def fixedPoint(self, A):
        l, r = 0, len(A) - 1
        while l < r:
            m = (l + r) / 2
            if A[m] - m < 0:
                l = m + 1
            else:
                r = m
        return l if A[l] == l else -1
