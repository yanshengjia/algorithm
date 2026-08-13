"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3


Solution:
1. DFS + Recursion
Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Depth First Search. During DFS, every visited node should be set as '0' to mark as visited node. Count the number of root nodes that trigger DFS, this number would be the number of islands since each DFS starting at some root identifies an island.

2. BFS + Queue/Stack
Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Breadth First Search. Put it into a queue and set its value as '0' to mark as visited node. Iteratively search the neighbors of enqueued nodes until the queue becomes empty.

3. Union Find
"""


# DFS Recursion
# Time: O(MN), M is the row number, N is the col number, since we visit each point one time.
# Space: worst case O(MN), in case that the grid map is filled with lands where DFS goes by M * N deep.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        res = 0
        row, col = len(grid), len(grid[0])
        visited = [[0 for _ in range(col)] for _ in range(row)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(x, y):
            visited[x][y] = 1   # mark the point visited when visiting it
            for dir in dirs:
                new_x, new_y = x + dir[0], y + dir[1]
                if 0 <= new_x < row and 0 <= new_y < col and visited[new_x][new_y] == 0 and grid[new_x][new_y] == '1':
                    dfs(new_x, new_y)

        
        # search
        for i in range(row):
            for j in range(col):
                if visited[i][j] == 0 and grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res


# DFS 
# Time: O(MN), M is the row number, N is the col number, since we visit each point one time.
# Space: worst case O(MN), in case that the grid map is filled with lands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # edge case
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        
        # dfs starting from coordinate (i, j)
        def dfs(i, j):
            # stop condition: index overflown or meet water or meet visited cell
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return
            
            grid[i][j] = '-1' # mark as visited

            # visit all adjavent cells
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)

        return num_islands


# DFS Iteration
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        res = 0
        row, col = len(grid), len(grid[0])
        visited = [[0 for _ in range(col)] for _ in range(row)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # search
        for i in range(row):
            for j in range(col):
                if visited[i][j] == 0 and grid[i][j] == '1':
                    res += 1
                    stack = [(i, j)]
                    visited[i][j] = 1   # mark the point when visiting, not when poping since some points will be pushed into stack repeatedly
                    while len(stack) > 0:
                        x, y = stack.pop(0)
                        
                        for dir in dirs:
                            new_x, new_y = x + dir[0], y + dir[1]
                            if 0 <= new_x < row and 0 <= new_y < col and visited[new_x][new_y] == 0 and grid[new_x][new_y] == '1':
                                visited[new_x][new_y] = 1   # mark the point when visiting, not when poping
                                stack.append((new_x, new_y))
        return res
    
        
# BFS
# Time: O(MN)
# Space: O(MN)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        res = 0
        row, col = len(grid), len(grid[0])
        visited = [[0 for _ in range(col)] for _ in range(row)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # bfs
        for i in range(row):
            for j in range(col):
                if visited[i][j] == 0 and grid[i][j] == '1':
                    res += 1
                    q = [(i, j)]
                    visited[i][j] = 1
                    for point in q:
                        x, y = point[0], point[1]

                        for dir in dirs:
                            new_x, new_y = x + dir[0], y + dir[1]
                            if 0 <= new_x < row and 0 <= new_y < col and visited[new_x][new_y] == 0 and grid[new_x][new_y] == '1':
                                visited[new_x][new_y] = 1
                                q.append((new_x, new_y))
        return res
        
        
# BFS (Stack)
# Time Complexity: O(MN), M is the row number, N is the col number, since we visit each point one time.
# Space Complexity: O(MN), in case that the grid map is filled with lands where
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # edge case
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        
        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1': # find a new island
                    num_islands += 1
                    grid[i][j] = 0 # mark as visited
                    neighbours = [(i, j)] # use stack to bfs

                    while neighbours:
                        row, col = neighbours.pop()

                        # up
                        if row - 1 >= 0 and grid[row-1][col] == '1':
                            grid[row-1][col] = 0 # mark as visited
                            neighbours.append((row-1, col))
                        # down
                        if row + 1 < m and grid[row+1][col] == '1':
                            grid[row+1][col] = 0 # mark as visited
                            neighbours.append((row+1, col))
                        # left
                        if col - 1 >= 0 and grid[row][col-1] == '1':
                            grid[row][col-1] = 0 # mark as visited
                            neighbours.append((row, col-1))
                        # right
                        if col + 1 < n and grid[row][col+1] == '1':
                            grid[row][col+1] = 0 # mark as visited
                            neighbours.append((row, col+1))
        
        return num_islands
