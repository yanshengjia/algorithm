"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13


Solution:
reverse inorder traversal
* recursive
* iterative + stack
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Iterative
# Time: O(N), where N is the tree size
# Space: O(N), worst case, totally unbalanced tree
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        sum = 0
        stack = []
        dummy = root
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.right   # right subtree first
            
            root = stack.pop()
            sum += root.val
            root.val = sum
            root = root.left    # left subtree second
        return dummy


# Recursive
# Time: O(N), where N is the tree size
# Space: O(N), Consider the worst case, a tree with only right (or only left) subtrees. The call stack will grow until the end of the longest path is reached, which in this case includes all N nodes.
class Solution:
    def __init__(self):
        self.sum = 0    # store the sum of vals of current visited nodes
    
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.convertBST(root.right)
            self.sum += root.val
            root.val = self.sum
            self.convertBST(root.left)
        return root
