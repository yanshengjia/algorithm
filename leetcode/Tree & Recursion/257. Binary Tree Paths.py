"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3


Solution:
1.DFS with recursion
2.BFS with stack [(node, current path)]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res, path = [], []
        self.dfs(root, path, res)
        return res
    
    def dfs(self, root, path, res):
        if root != None:
            path.append(root.val)
            if root.left == None and root.right == None:
                path = [str(i) for i in path]
                res.append('->'.join(path))
            if root.left:
                self.dfs(root.left, path, res)
                path.pop()
            if root.right:
                self.dfs(root.right, path, res)
                path.pop()


# BFS
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if root == None:
            return res
        
        stack = [(root, [root.val])]
        while len(stack) > 0:
            node, path = stack.pop()
            if node.left == None and node.right == None:
                path = [str(i) for i in path]
                res.append('->'.join(path))
            if node.left:
                path.append(node.left.val)
                stack.append((node.left, copy.deepcopy(path)))
                path.pop()
            if node.right:
                path.append(node.right.val)
                stack.append((node.right, copy.deepcopy(path)))
                path.pop()
        return res


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Time-O(N), where N is the number of nodes in tree
# Space-[O(logN), O(N)]  best situation: balanced tree, bad situation: we keep up to the entire tree
# faster than 99.36% in py3
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if root == None:
            return res
        
        stack = [(root, str(root.val))]
        while len(stack) > 0:
            node, path = stack.pop()
            if node.left == None and node.right == None:
                res.append(path)
            if node.left:
                stack.append((node.left, "{}->{}".format(path, node.left.val)))
            if node.right:
                stack.append((node.right, "{}->{}".format(path, node.right.val)))
        return res

            