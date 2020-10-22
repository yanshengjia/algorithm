"""
Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.


Example 1:
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Example 2:
Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Example 3:
Input: mat = [[5]]
Output: 5


Solution:
Please pay attention to the column number of matrix.
If it is odd, the center element should only be counted once.
If it is even, there is no center element.
"""


# Time: O(m), m = len(mat)
# Space: O(1)
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        res = 0
        for i in range(m):
            res += mat[i][i]
            res += mat[i][m-i-1]
        if m % 2:
            res -= mat[i//2][i//2]
        return res
