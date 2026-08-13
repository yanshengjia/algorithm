# Image courses are nodes, course dependencies are directed edges. 
# This problem is to find if there is a cycle in the directed graph (DAG). 
#   If there is a cycle, then it is impossible to finish all courses. 

# Topological Sort 
# Kahn's Algorithm (BFS)
# Time Complexity: O(V + E), where V is the number of courses (vertices) and E is the number of prerequisites (edges).
# Space Complexity: O(V + E), for storing the graph and indegree array.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph problem: detech cycle in DAG
        # Kahn's algorithm — BFS
        # course is node, course dependency is edge

        from collections import defaultdict

        # create a graph representation for courses and indegree array
        graph = defaultdict(list) # adjacency list: key is node, value is a list of key's neighboring nodes
        indegree = [0] * numCourses

        # build the graph and populate indegree array
        for dest, src in prerequisites:
            graph[src].append(dest)  # src -> dest, build adjacency list
            indegree[dest] += 1
        
        # init the stack with all courses that have no prerequisites (indegree = 0)
        stack = [i for i in range(numCourses) if indegree[i] == 0]

        completed_coursed = 0 # visited nodes

        while stack:
            course = stack.pop()
            completed_coursed += 1
        
            # decrease the indegress of neighboring courses
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                # if indegree becomes 0, add to stack
                if indegree[neighbor] == 0:
                    stack.append(neighbor)
        
        # if all courses are completed, no cycle in DAG
        return completed_coursed == numCourses
