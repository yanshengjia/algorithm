"""
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.


Example 1:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.


Solution:
Recursion
Let children know who their grandparent is.

Assume root has parent.val = 1 and grandparent.val = 1.
Recursive iterate the whole tree and pass on the value of parent and grandparent.
Count the root.val when grandparant if even-valued.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# DFS
# Time: O(N), N is the tree size
# Space: O(H), H is the tree height
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.dfs(root, 1, 1)
    
    def dfs(self, node, parent, grandparent):
        if node == None:
            return 0
        else:
            res = self.dfs(node.left, node.val, parent) + self.dfs(node.right, node.val, parent)
            if grandparent % 2 == 0:
                return res + node.val
            else:
                return res