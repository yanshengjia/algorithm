"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.


Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.


Solution:
Build a parent link of each node using Hashmap (key: node, value: parent node).
Convert this problem to a graph search problem.
Do BFS on graph.
One node has 3 pointers, left, right, parent
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# BFS
# Time: O(n), where n is the number of nodes in tree
# Space: O(n)
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # build parent link
        def dfs(node, parent=None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root)
        
        # bfs in the graph
        res = []
        queue = [(target, 0)]   # (node, distance to target)
        visited = {target}      # keep track of visited nodes, prevent duplicate visiting
        while len(queue) > 0:
            node, distance = queue.pop()
            visited.add(node)
            if distance == K:
                res.append(node.val)
            else:
                if node.left != None and node.left not in visited:
                    queue.append((node.left, distance + 1))
                if node.right != None and node.right not in visited:
                    queue.append((node.right, distance + 1))
                if node.parent != None and node.parent not in visited:
                    queue.append((node.parent, distance + 1))
        return res
