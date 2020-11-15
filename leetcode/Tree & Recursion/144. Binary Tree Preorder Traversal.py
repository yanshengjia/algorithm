"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

 
Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [1,2]

Example 5:
Input: root = [1,null,2]
Output: [1,2]


Solution:
* Recursion
* Iteration with Stack
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursion
# Time: O(N), N = tree size
# Space: O(N) in worst case, O(logN) in average case
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def preorderTraversalHelper(node):
            if node == None:
                return
            res.append(node.val)
            preorderTraversalHelper(node.left)
            preorderTraversalHelper(node.right)
        
        preorderTraversalHelper(root)
        return res


# Iteration with Stack
# Time: O(N)
# Space: O(N) in worst case, which is totally tilted
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        s = []
        
        while root != None or len(s) > 0:
            while root != None:
                s.append(root)
                res.append(root.val)
                root = root.left
            
            node = s.pop()
            root = node.right    
        return res
