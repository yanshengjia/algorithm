"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.


Solution:
Go over all diagonals.
"""


# Time: O(mn)
# Space: O(1)
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        for i in range(col):
            # start from (0, i)
            anchor = matrix[0][i]
            for j in range(1, row):
                if i + j >= col or j >= row:
                    break
                if matrix[j][i+j] != anchor:
                    return False
        
        for i in range(1, row):
            # start from (i, 0)
            anchor = matrix[i][0]
            for j in range(1, row-1):
                if i + j >= row or j >= col:
                    break
                if matrix[i+j][j] != anchor:
                    return False
        return True
