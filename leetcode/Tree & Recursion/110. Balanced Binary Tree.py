"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true


Solution:
* top-down recursion
* bottom-up recursion, faster!
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Top-down recursion
# Time: O(nlogn), https://leetcode.com/problems/balanced-binary-tree/solution/
# Space: O(n), the recursion stack may contain all nodes if the tree is skewed.
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    
    def height(self, node: TreeNode) -> int:
        if node == None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1


# Bottom-up recursion
# Time: O(N), N = tree size, faster than 92%
# Space: O(N), recursion stack may go up to O(N) if the tree is unbalanced
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]

    # return (is_balanced, tree_height)
    def isBalancedHelper(self, node: TreeNode) -> (bool, int):
        if node == None:
            return True, -1
        
        # post order traversal
        is_left_balanced, left_height = self.isBalancedHelper(node.left)
        if is_left_balanced == False:
            return False, 0
        is_right_balanced, right_height = self.isBalancedHelper(node.right)
        if is_right_balanced == False:
            return False, 0
        
        tree_height = max(left_height, right_height) + 1
        is_balanced = 1 if abs(left_height - right_height) < 2 else 0
        return is_balanced, tree_height
