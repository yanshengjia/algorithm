"""
Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:
Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]


Solution:
Reversed Inorder Traversal
right -> root -> left
record the sum of bigger nodes
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Iterative
# Time: O(n), n is the number of nodes
# Space: O(n), worst case
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        dummy = root
        sum = 0
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.right
            
            root = stack.pop()
            sum += root.val
            root.val += (sum - root.val)
            root = root.left
        
        return dummy
        