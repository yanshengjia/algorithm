"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---


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
# Time: O(n), n is the number of tree node
# Space: O(n), worst case
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        res = [root.val]
        level = [root]
        while level:
            cache = []
            for node in level:
                if node.left:
                    cache.append(node.left)
                if node.right:
                    cache.append(node.right)
            
            if cache:
                res.append(cache[-1].val)
                level = cache
            else:
                break
        return res
