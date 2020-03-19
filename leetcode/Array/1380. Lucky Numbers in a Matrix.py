"""
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.


Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]


Solution:
3 Pass
"""


# Time: O(mn)
# Spcae: O(m+n)
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        
        row_min = []
        col_max = []
        
        for i in range(row):
            mi = float('inf')
            for j in range(col):
                mi = min(matrix[i][j], mi)
            row_min.append(mi)
        
        for j in range(col):
            ma = float('-inf')
            for i in range(row):
                ma = max(matrix[i][j], ma)
            col_max.append(ma)
        
        res = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == row_min[i] and matrix[i][j] == col_max[j]:
                    res.append(matrix[i][j])
        return res


# 3 Pass
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rmin = [min(x) for x in matrix]
        cmax = [max(x) for x in zip(*matrix)]
        return [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0])) if rmin[i] == cmax[j]]