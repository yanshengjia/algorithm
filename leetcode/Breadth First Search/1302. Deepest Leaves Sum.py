"""
Given a binary tree, return the sum of values of its deepest leaves.
 
Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15


Solution:
BFS Level-order traversal
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# BFS
# Time: O(N), N is the tree size
# Space: O(x), x is the number of nodes of the level which has the most nodes
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        level = [root]
        cache = []
        while level:
            sum = 0
            for node in level:
                sum += node.val
                if node.left:
                    cache.append(node.left)
                if node.right:
                    cache.append(node.right)
            level = cache
            cache = []
        return sum
