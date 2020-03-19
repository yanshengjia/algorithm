"""
Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if it's parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you can't).


Example 1:
Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).

Example 2:
Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]

Example 3:
Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.

Example 4:
Input: root = [1,1,1], target = 1
Output: []

Example 5:
Input: root = [1,2,3], target = 1
Output: [1,2,3]


Solution:
Recursion
Recursively call removeLeafNodes on the left and right.
If root.left == root.right == null and root.val == target,
the root node is now a leaf with value = target, we return null.
Otherwise return root node itself.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursion
# Time: O(N), N is the tree size
# Space: O(H), H is the tree height for the recursion stack
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root == None:
            return None
        
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
        
        if root.left == None and root.right == None and root.val == target:
            return None
        else:
            return root
        