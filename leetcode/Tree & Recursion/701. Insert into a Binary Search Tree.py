"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4


Solution:
1. Recursion
2. Iteration
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursion
# Time: O(H), H is the tree height, O(N) at worst case
# Space: O(H) to keep the recursion stack, O(N) at worst case
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
    

# Iteration
# Time: O(H) avg case, O(N) worst case
# Space: O(1)
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node:
            if val > node.val:
                # insert to right subtree
                if node.right == None:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right
            else:
                # insert to left subtree
                if node.left == None:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
        return root        


