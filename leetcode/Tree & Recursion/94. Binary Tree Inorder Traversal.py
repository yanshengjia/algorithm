"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [2,1]

Example 5:
Input: root = [1,null,2]
Output: [1,2]


Solution:
* Recursion
* Iteration
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursion
# Time: O(N)
# Space: O(N) in the worst case, O(logN) in the average case
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def inorderTraversalHelper(node):
            if node == None:
                return
            inorderTraversalHelper(node.left)
            res.append(node.val)
            inorderTraversalHelper(node.right)
        
        inorderTraversalHelper(root)
        return res


# Iteration with Stack
# Time: O(N), N = tree size
# Space: O(N)
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        s = []
        while root != None or len(s) > 0:
            while (root != None):
                s.append(root)
                root = root.left
            
            node = s.pop()
            res.append(node.val)
            root = node.right
        return res