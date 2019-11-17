"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6


Solution:
1. Recursion
2. Iteration
"""


# DFS Recursion
# Time: O(N)
# Space: O(H) = O(logN), h is the tree depth, to keep the recursion stack
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return 1 + self.countNodes(root.right) + self.countNodes(root.left) if root else 0


# BFS Iteration + Queue
# Time: O(N)
# Space: O(N)
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        res = 1
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                res += 1
            if node.right:
                queue.append(node.right)
                res += 1
        
        return res
