"""
Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is, always ones may appear first and then zeros.


Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]

Explanation: 
The number of soldiers for each row is: 
row 0 -> 2 
row 1 -> 4 
row 2 -> 1 
row 3 -> 2 
row 4 -> 5 
Rows ordered from the weakest to the strongest are [2,0,3,1,4]


Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]

Explanation: 
The number of soldiers for each row is: 
row 0 -> 1 
row 1 -> 4 
row 2 -> 1 
row 3 -> 1 
Rows ordered from the weakest to the strongest are [0,2,3,1]


Solution:
1. Linear Search + Sort
* TC: O(MN + MlogM), M = row number, N = column number
* SC: O(M)
2. Binary Search + Sort   Faster to count 1 in the row
* TC: O(MlogN + MlogM) = O(MlogMN), M = row number, N = column number
* SC: O(M)
"""


# Linear Search + Sort
# TC: O(MN + MlogM), M = row number, N = column number
# SC: O(M)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = len(mat)
        d = {}
        res = []
        
        for i in range(rows):
            d[i] = mat[i].count(1)
        
        d = sorted(d.items(), key=lambda kv: kv[1])
        
        for i in range(k):
            res.append(d[i][0])
        
        return res


# Binary Search + Sort
# TC: O(MlogN + MlogM) = O(MlogMN), M = row number, N = column number
# SC: O(M)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = {}
        res = []
        
        for i in range(len(mat)):
            leftmost_0_index = self.binary_search(mat[i])
            d[i] = leftmost_0_index
        
        d = sorted(d.items(), key=lambda kv: kv[1])
        
        for i in range(k):
            res.append(d[i][0])
        
        return res
    
    # find the leftmost 0 index
    def binary_search(self, row):
        low, high = 0, len(row)
        
        while low < high:
            mid = (low + high) // 2
            if row[mid] == 1:
                low = mid + 1
            else:
                high = mid
        return low
