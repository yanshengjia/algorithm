"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.


Solution:
Detect circle in the DAG, convert Graph to adjacency list

1. BFS + Topological Sort
BFS uses the indegrees of each node. We will first try to find a node with 0 indegree. If we fail to do so, there must be a cycle in the graph and we return false. Otherwise we set its indegree to be -1 to prevent from visiting it again and reduce the indegrees of its neighbors by 1. This process will be repeated for n (number of nodes) times.
If we can finish all courses, the graph always has at least one node with indegree 0 during the BFS process.

2. DFS
For DFS, in each visit, we start from a node and keep visiting its neighbors, if at a time we return to a visited node, there is a cycle. Otherwise, start again from another unvisited node and repeat this process.

if node v has not been visited, then mark it as 0.
if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then there is a ring.
if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.
"""


# BFS + Topological Sort
# Time: O(V+E)
# Space: O(V+E)
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.build_graph(prerequisites)
        indegrees = self.compute_indegrees(graph, numCourses)
        
        # repeat n times
        for i in range(numCourses):
            # find the course with indegree 0, that's the first course we need to take
            j = 0
            while j < numCourses:
                if indegrees[j] == 0:
                    break
                j += 1
            
            if j == numCourses:
                # no course has indegree 0, i.e. a circle in graph
                return False
            
            indegrees[j] = -1 # prevent from visiting it again
            for node in graph[j]:
                # reduce the indegrees of its neighbors by 1
                indegrees[node] -= 1
        return True    
        
    def build_graph(self, prerequisites):
        # convert to adjacency list
        graph = collections.defaultdict(list)
        for p in prerequisites:
            graph[p[1]].append(p[0])
        return graph
    
    def compute_indegrees(self, graph, numCourses):
        indegrees = [0 for _ in range(numCourses)]
        
        for k, adj in graph.items():
            for node in adj:
                indegrees[node] += 1
        return indegrees
        

# DFS
# if node v has not been visited, then mark it as 0.
# if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then there is a ring.
# if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.
# Time: O(V+E)
# Space: O(V+E)
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.build_graph(prerequisites)
        visited = [0 for _ in range(numCourses)]
        
        # visit each node
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True   
        
    def build_graph(self, prerequisites):
        # convert to adjacency list
        graph = collections.defaultdict(list)
        for p in prerequisites:
            graph[p[1]].append(p[0])
        return graph
    
    def dfs(self, graph: dict, visited: list, node: int) -> bool:
        # return False means there is a ring
        
        if visited[node] == -1:
            # node is marked as being visited, there is a ring
            return False
        
        if visited[node] == 1:
            # node is done visited, then do not visit again
            return True
        
        # node is being visited
        visited[node] = -1
        
        for neighbour in graph[node]:
            if not self.dfs(graph, visited, neighbour):
                return False
        
        # after visit all the neighbours, mark node as done visited
        visited[node] = 1
        return True
