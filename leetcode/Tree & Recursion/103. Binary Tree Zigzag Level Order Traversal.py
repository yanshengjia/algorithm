"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        level_num = 0
        res = [[root.val]]
        stack = [root]
        next_level = []
        next_level_val = []
        while len(stack) > 0:
            node = stack.pop()  # pop from top
            if level_num % 2 == 0:
                if node.right != None:
                    next_level.append(node.right)
                    next_level_val.append(node.right.val)
                if node.left != None:
                    next_level.append(node.left)
                    next_level_val.append(node.left.val)
            else:
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
                level_num += 1
        return res