"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]


Solution:
1.DFS recursion
2.BFS queue
3.DFS stack
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS + Recursion
import copy
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path, s = [], [], 0
        self.dfs(root, path, s, sum, res)
        return res
        
    def dfs(self, root, path, s, sum, res):
        if root:
            s += root.val
            path.append(root.val)
            if s == sum and root.left == None and root.right == None:
                res.append(copy.deepcopy(path))
            if root.left:
                self.dfs(root.left, path, s, sum, res)
            if root.right:
                self.dfs(root.right, path, s, sum, res)
            s -= path.pop()
