"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.


Example 1:

Input: [1,1,1,1,1,null,1]
Output: true
Example 2:

Input: [2,2,2,5,2]
Output: false


Solution:
1. DFS Recursion
2. DFS Iteration
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# DFS Recursion
# Time: O(N), >40%, where N is the tree size
# Space: O(H), where H is the height of tree
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        if root.left:
            if root.val != root.left.val:
                return False
        
        if root.right:
            if root.val != root.right.val:
                return False
        
        l = self.isUnivalTree(root.left)
        r = self.isUnivalTree(root.right)
        return l and r


# DFS Recursion
# preorder traversal puting values in a set and returning if set.size() == 1
# Time: O(N), >80%
# Space: O(N)
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        nodes = []
        
        def dfs(node):
            if node:
                nodes.append(node.val)
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return len(set(nodes)) == 1


# DFS Iteration preorder traversal
# Time: O(N), >10%
# Space: O(N)
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        vals, cache = [], []
        
        # preorder traversal
        while root or len(cache) > 0:
            while root != None:
                vals.append(root.val)
                cache.append(root)
                root = root.left

            root = cache.pop()
            root = root.right
            
        return len(set(vals)) == 1