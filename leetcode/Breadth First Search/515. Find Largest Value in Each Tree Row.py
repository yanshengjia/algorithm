"""
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]


Solution:
1. BFS
2. DFS
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# BFS
# Time: O(n), n is tree size
# Space: O(n) at worst case
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        level = [root]
        res = [root.val]
        while level:
            cache_node = []
            cache_val = []
            for node in level:
                if node.left:
                    cache_node.append(node.left)
                    cache_val.append(node.left.val)
                if node.right:
                    cache_node.append(node.right)
                    cache_val.append(node.right.val)
            
            if cache_node:
                res.append(max(cache_val))
            level = cache_node
        return res
