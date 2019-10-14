"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1


Solution:
1. Recursion
2. Iterative
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursion
# Time: O(N), where N is the tree size
# Space: O(N), O(h) function calls will be placed on the stack in the worst case, where h is the height of the tree. Since h is O(n), the space complexity is O(n)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root
        

# Iteration
# Swap left child and right child of each notnull node
# Time: O(N), where N is the tree size
# Space: O(N), since in the worst case, the queue will contain all nodes in one level of the binary tree. For a full binary tree, the leaf level has N/2 = O(N) leaves
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        
        stack = [root]
        while stack:
            node = stack.pop()
            left = node.left
            right = node.right
            node.left = right
            node.right = left
            if left != None:
                stack.append(left)
            if right != None:
                stack.append(right)
        
        return root
        



