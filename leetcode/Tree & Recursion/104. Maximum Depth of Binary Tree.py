"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.


Solution:
1. DFS + Recursion
2. BFS + Stack
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# DFS + Recursion
# Time-O(N), N is the number of nodes in the tree
# Space-[O(logN), O(N)], best case: balanced tree, O(logN), worst case: each node has only one left child
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
        

# Iteration: DFS + Stack
# Time-O(N), N is the number of nodes in the tree
# Space-[O(logN), O(N)], best case: balanced tree, O(logN), worst case: each node has only one left child
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        stack = []
        if root != None:
            stack.append((1, root))
        
        depth = 0
        while len(stack) > 0:
            cur_depth, node = stack.pop()
            depth = max(depth, cur_depth)
            if node.left:
                stack.append((cur_depth+1, node.left))
            if node.right:
                stack.append((cur_depth+1, node.right))
        return depth


# Iteration: BFS + Queue
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue   
        return depth