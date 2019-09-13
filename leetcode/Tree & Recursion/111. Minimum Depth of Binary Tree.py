"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.


Solution:
1. DFS Recursively
2. DFS Iteratively
3. BFS Iteratively -> Fastest
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# DFS Recursively
# The intuitive approach is to solve the problem by recursion. Here we demonstrate an example with the DFS (Depth First Search) strategy.
# Time: O(N), >45%, where N is the size of tree
# Space: O(logN) for a balanced tree. In the worst case, the storage to keep the call stack would be O(N)
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        child = [root.left, root.right]
        if not any(child):
            return 1
        
        min_depth = float('inf')
        for c in child:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1


# DFS Iteration
# We could also convert the above recursion into iteration, with the help of stack.
# The idea is to visit each leaf with the DFS strategy, while updating the minimum depth when we reach the leaf node.
# So we start from a stack which contains the root node and the corresponding depth which is 1. Then we proceed to the iterations: pop the current node out of the stack and push the child nodes. The minimum depth is updated at each leaf node.
# Time: O(N) since each node is visited exactly once
# Space: in the worst case we keep up tp the entire tree, s.t. O(N)
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        min_depth = float('inf')
        stack = [(root, 1)]
        
        while stack:
            root, depth = stack.pop()
            children = [root.left, root.right]
            if not any(children):   # update the min-depth at leaf node
                min_depth = min(min_depth, depth)
            else:
                for c in children:
                    if c:
                        stack.append((c, depth + 1))
        return min_depth


# BFS Iteratin (Best)
# The drawback of the DFS approach in this case is that all nodes should be visited to ensure that the minimum depth would be found. Therefore, this results in a \mathcal{O}(N)O(N) complexity. One way to optimize the complexity is to use the BFS strategy. We iterate the tree level by level, and the first leaf we reach corresponds to the minimum depth. As a result, we do not need to iterate all nodes.
# Time: >97%, in the worst case for a balanced tree we need to visit all nodes level by level up to the tree height, that excludes the bottom level only. This way we visit N/2 nodes, and thus the time complexity is O(N)
# Space: O(N)
from collections import deque

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        node_deque = deque([(root, 1)])
        
        while node_deque:
            root, depth = node_deque.popleft()
            children = [root.left, root.right]
            if not any(children):   # return the min-depth at leaf node
                return depth
            else:
                for c in children:
                    if c:
                        node_deque.append((c, depth + 1))



