"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].


Solution:
1. DFS
DFS the tree and record the value of node with its level.
2. BFS
level-order traversal
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# BFS
# Time: O(N), N is the tree size
# Space: O(M), The size of queue can grow upto atmost the maximum number of nodes at any level in the given binary tree. Here, mm refers to the maximum mumber of nodes at any level in the input tree.
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root == None:
            return []
        
        level = [root]
        cache = []
        res = [root.val]
        while len(level) > 0:
            s = 0
            for node in level:
                if node.left:
                    cache.append(node.left)
                    s += node.left.val
                if node.right:
                    cache.append(node.right)
                    s += node.right.val
            
            level = cache
            if len(cache) > 0:
                res.append(s / len(cache))
                cache = []
                
        return res
