"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

Solution:
1. DFS + Stack
2. BFS + Queue
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# BFS
# Time: O(n), n is tree size
# Space: O(n), worst case
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if root == None:
            return []
        
        level = [root]
        while level:
            cache = []
            for node in level:
                if node.left:
                    cache.append(node.left)
                if node.right:
                    cache.append(node.right)
            
            if cache:
                level = cache
            else:
                break
        return level[0].val
        