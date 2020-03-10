"""
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example:

Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]
 

Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         / 
        2          
 

2. Now removing the leaf [2] would result in this tree:

          1          
 

3. Now removing the leaf [1] would result in the empty tree:

          []         


Solution:
DFS
Put nodes with same level order together.
Leave order = 1, order += 1 every level up
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# DFS
# Use DFS to find the level order of each node
# Time: O(N), N is the number of nodes in the tree
# Spacr: O(N)
import collections
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        d = collections.defaultdict(list)
        
        # leave order = 1, order += 1 every level up
        def order(root):
            if not root:
                return 0
            left = order(root.left)
            right = order(root.right)
            level = max(left, right) + 1
            d[level].append(root.val)
            return level
        
        res = []
        order(root)
        for i in range(1, len(d) + 1):
            res.append(d[i])
        return res
        