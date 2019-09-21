"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.


Solution:
1. Preorder Traversal to build a string
2. By comparsion of nodes
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Preorder Traversal to build a string
# Time: O(M+N+MN), where M is the size of tree s, N is the size of tree t, O(M) and O(N) for each tree and O(MN) for the substring search
# Space: O(M+N)
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        preorder_s = self.preorder(s)
        preorder_t = self.preorder(t)
        return preorder_t in preorder_s
    
    
    def preorder(self, root):
        if root == None:
            return []
        nodes, cache = "", []
        
        while len(cache) or root > 0:
            while root != None:
                nodes += "#" + str(root.val)
                cache.append(root)
                root = root.left
            root = cache.pop()
            if root.left == None and root.right == None:
                nodes += "lnull#rnull#"
            elif root.left == None and root.right != None:
                nodes += "lnull#"
            elif root.left != None and root.right == None:
                nodes += "rnull#"
            root = root.right
        return nodes
        
        

# Inorder Traversal
# Time: O(M+N), >97%, where M is the size of tree s, N is the size of tree t
# Space: O(M+N), >100%
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        preorder_s = self.inorder(s)
        preorder_t = self.inorder(t)
        return preorder_t in preorder_s
    
    
    def inorder(self, root):
        if root == None:
            return []
        nodes, cache = "", []
        
        while len(cache) > 0 or root != None:
            while root != None:
                cache.append(root)
                root = root.left
            root = cache.pop()
            nodes += "#" + str(root.val)
            if root.left == None and root.right == None:
                nodes += "lnull#rnull#"
            elif root.left == None and root.right != None:
                nodes += "lnull#"
            elif root.left != None and root.right == None:
                nodes += "rnull#"
            root = root.right
        return nodes
        
        
# DFS + Recursion
# Time: O(M+N+MN)
# Space: O(M+N)
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def dfs(root):
            if root is None:
                return 'None'
            tmp = str(root.val) + ','+ dfs(root.left) + ','+  dfs(root.right)   # preorder
            return ','+tmp+','
        return dfs(s).find(dfs(t)) >= 0
        
        
        
         
        
        
        
        