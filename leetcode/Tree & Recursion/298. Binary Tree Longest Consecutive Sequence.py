"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.


Solution:
It's actually longest ascending consective sequence path
1. Recursion
* top-down tail recursion
* bottom-up non-tail recursion
2. Iteration
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# top-down DFS, like preorder traversal
# Time: O(n), n is the tree size
# Space: O(n). The extra space comes from implicit stack space due to recursion. For a skewed binary tree, the recursion could go up to n levels deep.
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        length = 0
        self.max_length = 0
        self.dfs(root, None, length)
        return self.max_length
    
    
    # preorder traversal
    def dfs(self, node, parent, length):  # node is the child of parent
        if node == None:
            return
        
        # check if consecutive
        if parent != None and node.val == parent.val + 1:
            length += 1
        else:
            length = 1
        
        # update max_length
        self.max_length = max(self.max_length, length)
        
        # top-down dfs
        self.dfs(node.left, node, length)
        self.dfs(node.right, node, length)
        
        
# Bottom-up DFS, like postorder traversal
# Time: O(n), n is the tree size
# Space: O(n). The extra space comes from implicit stack space due to recursion. For a skewed binary tree, the recursion could go up to n levels deep.
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.max_length = 0
        self.dfs(root)
        return self.max_length
    
    
    # postorder traversal
    def dfs(self, node):
        if node == None:
            return 0
        
        # bottom-up dfs
        l = self.dfs(node.left) + 1
        r = self.dfs(node.right) + 1
        
        # check if consecutive
        if node.left != None and node.val + 1 != node.left.val:
            l = 1
        if node.right != None and node.val + 1 != node.right.val:
            r = 1
        
        length = max(l, r)
        self.max_length = max(self.max_length, length)
        return length     


# Iterative Breadth-First Search
# BFS queue popleft
from collections import deque
def longestConsecutive(self, root):
    if not root:
        return 0
    ans, dq = 0, deque([[root, 1]])
    while dq:
        node, length = dq.popleft()
        ans = max(ans, length)
        for child in [node.left, node.right]:
            if child:
                l = length + 1 if child.val == node.val + 1 else 1
                dq.append([child, l])
    return ans


# Iterative Depth-First Search
# DFS stack popright
def longestConsecutive(self, root):
    if not root:
        return 0
    ans, stack = 0, [[root, 1]]
    while stack:
        node, length = stack.pop()
        ans = max(ans, length)
        for child in [node.left, node.right]:
            if child:
                l = length + 1 if child.val == node.val + 1 else 1
                stack.append([child, l])
    return ans
