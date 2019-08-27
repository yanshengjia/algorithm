"""
In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]


Solution:
Row and Column Maximums.
The height of the building (i, j) can be increased is min(max_height_in_row, max_height_in_col)
"""


# Time: O(N^2), where N is the number of rows (and columns) of the grid. We iterate through every cell of the grid.
# Space: O(N), the space used by row_maxes and col_maxes.
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        res = 0 
        row_len, col_len = len(grid[0]), len(grid)
        max_row = [0] * row_len
        max_col = [0] * col_len
        
        for i in range(col_len):
            max_row[i] = max(grid[i])
        for j in range(row_len):
            max_col[j] = max([grid[i][j] for i in range(col_len)])
        
        for i in range(col_len):
            for j in range(row_len):
                res += min(max_row[i], max_col[j]) - grid[i][j]
        return res