"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23


Solution:
DFS
* recursive with tree pruning
* iterative with stack

x-axis: dfs(right)  L  dfs(left) dfs(right)  R  dfs(left)
node.val < R : dfs(right)
node.val > L : dfs(left)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursion with tree pruning
# time-O(n)  n is the number of nodes in the tree
# space-O(1)
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.res = 0
        self.dfs(root, L, R)
        return self.res
    
    def dfs(self, root, L, R):
        if root:
            if L <= root.val <= R:
                self.res += root.val
                self.dfs(root.left, L, R)
                self.dfs(root.right, L, R)
            elif root.val < L:  # tree pruning
                self.dfs(root.right, L, R)
            else:  # tree pruning
                self.dfs(root.left, L, R)
    
    def dfs_2(self, root, L, R):
        if root:
            if L <= root.val <= R:
                self.res += root.val
            if root.val > L:
                self.dfs(root.left, L, R)
            if root.val < R:
                self.dfs(root.right, L, R)
        

# iterative implementation
# time-O(n), where n is the number of nodes in the tree
# space-O(H), where H is the height of the tree.       
class Solution(object):
    def rangeSumBST(self, root, L, R):
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans     
        
