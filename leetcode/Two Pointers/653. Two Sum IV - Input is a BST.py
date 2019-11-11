"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
 

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False


Solution:
1. Output BST to array. Convert it to normal 2Sum problem. Hashtable, Two Pointers.
2. Inorder Traversal + Hashtable
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Inorder + Hashtable
# Time: O(n), n is the number of tree nodes
# Space: O(n), worst case
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        d = dict()
        
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if root.val in d:
                return True
            d[k - root.val] = 1
            root = root.right
        return False
        