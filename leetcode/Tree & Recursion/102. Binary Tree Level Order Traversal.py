"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]


Solution:
1. DFS
2. BFS
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# BFS + Stack
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = [[root.val]]
        stack = [root]
        next_level = []
        next_level_val = []
        while len(stack) > 0:
            node = stack.pop(0)
            if node.left != None:
                next_level.append(node.left)
                next_level_val.append(node.left.val)
            if node.right != None:
                next_level.append(node.right)
                next_level_val.append(node.right.val)
            if len(stack) == 0:
                if len(next_level_val) > 0:
                    res.append(next_level_val)
                stack = next_level
                next_level = []
                next_level_val = []
        return res
        
        
        