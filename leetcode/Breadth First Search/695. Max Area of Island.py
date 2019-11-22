"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.


Solution:
1. DFS Recursion
2. DFS + Stack
3. BFS + Queue
"""


# DFS Recursion
# Time: O(MN)
# Space: O(MN)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[0 for _ in range(col)] for _ in range(row)]
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def bfs(r, c):
            self.area += 1
            visited[r][c] = 1
            for dir in dirs:
                new_r = r + dir[0]
                new_c = c + dir[1]
                if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] == 1 and visited[new_r][new_c] == 0:
                    bfs(new_r, new_c)
                    visited[new_r][new_c] = 1
        
        max_area = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    self.area = 0
                    bfs(i, j)
                    if self.area > max_area:
                        max_area = self.area
        return max_area


# DFS + Stack
# Time: O(MN)
# Space: O(MN)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[0 for _ in range(col)] for _ in range(row)]
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]            
        
        max_area, area = 0, 0
        stack = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    area = 0
                    stack = [(i, j)]
                    
                    while stack:
                        r, c = stack.pop()
                        area += 1
                        visited[r][c] = 1
                        for dir in dirs:
                            new_r = r + dir[0]
                            new_c = c + dir[1]
                            if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] == 1 and visited[new_r][new_c] == 0:
                                stack.append((new_r, new_c))
                                visited[new_r][new_c] = 1   # mark here
                                

                    if area > max_area:
                        max_area = area
        return max_area
            
        
# BFS + Queue
# Time: O(MN)
# Space: O(MN)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[0 for _ in range(col)] for _ in range(row)]
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]            
        
        max_area, area = 0, 0
        queue = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    area = 0
                    queue = [(i, j)]
                    
                    while queue:
                        r, c = queue.pop(0)
                        area += 1
                        visited[r][c] = 1
                        for dir in dirs:
                            new_r = r + dir[0]
                            new_c = c + dir[1]
                            if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] == 1 and visited[new_r][new_c] == 0:
                                queue.append((new_r, new_c))
                                visited[new_r][new_c] = 1   # mark here
                                

                    if area > max_area:
                        max_area = area
        return max_area
