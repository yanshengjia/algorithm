"""
Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.


Example 1:
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]


Solution:
A[i][j] on the same diagonal have same value of i-j
For each diagonal, put its elements in the same list, sort and put them back.
"""


# sort diagonally
# Time: O(mnlogD), where D = min(m, n) len of diagonal
# Space: O(mn)
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = {}
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            for j in range(n):
                if i - j not in d:
                    d[i-j] = [mat[i][j]]
                else:
                    d[i-j].append(mat[i][j])
        
        for k in d:
            d[k].sort(reverse=1)
        
        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i-j].pop()
        return mat
