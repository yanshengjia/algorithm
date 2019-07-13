"""
Description:
Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.
A valid path is from root node to any of the leaf nodes.

Solution:
DFS recursive
在遍历树的同时需要记录根结点到当前节点的路径与累计和
注意 list 的 append() 是浅拷贝，需要用 copy 的 deepcopy
当 list 类型的对象进行 append 操作时，实际上追加的是该对象的引用。所以当 path 内容发生改变，res 也会改变。
"""


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import copy

class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        res = []
        path = []
        if root == None:
            return res
        self.findPath(root, target, 0, path, res)
        return res
        
    def findPath(self, root, target, now, path, res):
        now += root.val
        path.append(root.val)
        if now == target and root.left == None and root.right == None:
            res.append(copy.deepcopy(path))
        if root.left:
            self.findPath(root.left, target, now, path, res)
            path.pop()
        if root.right:
            self.findPath(root.right, target, now, path, res)
            path.pop()
