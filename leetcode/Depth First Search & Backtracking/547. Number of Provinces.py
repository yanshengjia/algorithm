"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.


Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 
Constraints:
* 1 <= n <= 200
* n == isConnected.length
* n == isConnected[i].length
* isConnected[i][j] is 1 or 0.
* isConnected[i][i] == 1
* isConnected[i][j] == isConnected[j][i]


Solution:
The given matrix can be viewed as the Adjacency Matrix of a graph. By viewing the matrix in such a manner, 
our problem reduces to the problem of finding the number of connected components in an undirected graph.
* DFS
* BFS
* Union Find
"""


# DFS
# TC: O(N^2), The complete matrix of size N^2 is traversed
# SC: O(N), visited array of size N is used
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        province = 0
        
        def dfs(city_i):
            for city_j in range(n):
                # if city_i is connected with city_j, target to city_j 
                if isConnected[city_i][city_j] == 1 and visited[city_j] == 0:
                    visited[city_j] = 1
                    dfs(city_j)  # search from city_j
        
        for city_i in range(n):
            if visited[city_i] == 0:
                dfs(city_i)
                province += 1
        return province


# BFS
# TC: O(N^2), The complete matrix of size N^2 is traversed
# SC: O(N), A queue and visited array of size N is used
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        province = 0
        
        # imagine provinces as a "tree" with loops 
        # use queue for BFS
        queue = []
        for city_i in range(n):
            if visited[city_i] == 0:  # city_i is not visited, bfs
                queue.append(city_i)
                while queue:
                    city_p = queue.pop()
                    visited[city_p] = 1
                    for city_j in range(n):
                        if isConnected[city_p][city_j] == 1 and visited[city_j] == 0:
                            queue.append(city_j)
                province += 1
        return province
