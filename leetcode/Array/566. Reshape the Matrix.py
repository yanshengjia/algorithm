"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the row number and column number of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.


Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
 

Constraints:
* m == mat.length
* n == mat[i].length
* 1 <= m, n <= 100
* -1000 <= mat[i][j] <= 1000
* 1 <= r, c <= 300


Solution:
Flatten and Reconstruct
* 2d -> 1d: M[i][j]=M[n*i+j] , where n is the number of cols. This is the one way of converting 2-d indices into one 1-d index.
* 1d -> 2d: M[i] => M[i/n][i%n]
"""


# TC: O(mn), where m = row number of matrix, n = col number of matrix
# SC: O(mn)
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        
        flat = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                flat[n * i + j] = mat[i][j]
        
        res = [[0] * c for _ in range(r)]
        for i in range(len(flat)):
            res[i // c][i % c] = flat[i]
            
        return res
