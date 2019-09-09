"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


Solution:
BST 的性质：
* 左子树中的所有节点 < 根结点 < 右子树中的所有节点
* 中序遍历得 non-decsending array

1. Recursion
2. Iteration
3. Inorder Traversal
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursion
# Time: O(N), >60%, where N is the size of tree
# Space: O(N), since we keep up to the entire tree
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, float('-inf'), float('inf'))
    
    
    def dfs(self, root, mn, mx):
        if root == None:
            return True
        if root.val <= mn or root.val >= mx:
            return False
        return self.dfs(root.left, mn, root.val) and self.dfs(root.right, root.val, mx)
        

# Iteration
# Time: O(N), >58%, where N is the size of tree
# Space: O(N), since we keep up to the entire tree
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        stack = [(root, float('-inf'), float('inf'))]
        
        # iteratively
        while stack:
            root, mn, mx = stack.pop()
            if root == None:
                continue
            if root.val <= mn or root.val >= mx:
                return False
            stack.append((root.left, mn, root.val))
            stack.append((root.right, root.val, mx))
        return True


# inorder
# Time: O(N), >6%, where N is the size of BST
# Space: O(N)
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.inorder(root) == sorted(list(set(self.inorder(root))))
    
    def inorder(self, root):
        if root == None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
        

# inorder without storing the array
# Time: O(N), >81%, where N is the size of BST
# Space: O(N)
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, pre = [], float('-inf')
        
        # inorder traversel iteratively
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            # cur element is supposed to be bigger than the previous one in a bst
            if root.val <= pre:
                return False
            pre = root.val
            root = root.right
        
        return True
        
        
        
        
        