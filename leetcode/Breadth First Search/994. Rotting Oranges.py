"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


Solution:
BFS
"""


# BFS
# Time: O(mn+mn+mn) = O(mn), m, n is the side length
# Space: O(mn), worst case
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        visited = set()
        queue, new_queue = [], []
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # first find all initial rotten oranges
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        time = 0
        
        # bfs
        while queue:
            node = queue.pop(0)
            visited.add(node)
            
            for dir in dirs:
                new_row = node[0] + dir[0]
                new_col = node[1] + dir[1]
                if 0 <= new_row < row and 0 <= new_col < col and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                    grid[new_row][new_col] = 2
                    visited.add((new_row, new_col))
                    new_queue.append((new_row, new_col))
            
            if len(queue) == 0 and len(new_queue) > 0:
                time += 1
                queue = new_queue
                new_queue = []
        
        # final check
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return time
