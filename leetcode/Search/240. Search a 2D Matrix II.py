"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.


Solution:
1. Brute Force  Time: O(mn)
2. Binary Search  Time: O(lg(n!))
3. Search Space Redction  Time: O(m+n)  Starting point: bottom-left point
"""


# Brute Force
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == target:
                    return True
        return False
        

# Binary Search, iterate over Matrix Diagonal
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        row, col = len(matrix), len(matrix[0])
        
        # iterate over matrix diagonals, from top-left to bottom-right
        short_edge = min(row, col)
        for i in range(short_edge):
            row_found = self.binary_search(matrix, target, i, False)
            col_found = self.binary_search(matrix, target, i, True)
            if row_found or col_found:
                return True
        return False
        
    
    def binary_search(self, matrix, target: int, start: int, vertical: bool) -> bool:
        lo = start
        hi = len(matrix) - 1  if vertical else len(matrix[0]) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if vertical:    # search column
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True
            else:   # search row
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
        return False


# Search Space Reduction
# Time: O(m+n)
# Space: O(1)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        row, col = len(matrix), len(matrix[0])
        x, y = row - 1, 0   # bottom-left point
        
        while x >= 0 and y < col:
            if matrix[x][y] > target:   # go up
                x -= 1
            elif matrix[x][y] < target: # go right
                y += 1
            else:
                return True
        return False
