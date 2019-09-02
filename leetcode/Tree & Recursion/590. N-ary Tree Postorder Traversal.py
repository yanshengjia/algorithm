"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:

   1
  /|\
 3 2 4
/ \
5  6

Return its postorder traversal as: [5,6,3,2,4,1].

Follow up:
Recursive solution is trivial, could you do it iteratively?


Solution:
1. Recursion
2. Iteration
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# Recursion
# Time: O(N), >65%, where N is the size of tree
# Space: O(N)
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self.dfs(root, res)
        return res
    
    def dfs(self, root, res):
        if root == None:
            return
        if len(root.children) == 0:
            res.append(root.val)
        else:
            for child in root.children:
                self.dfs(child, res)
            res.append(root.val)


# Iterative + Stack
# Time: O(N), >65%, where N is the size of tree
# Space: O(N)
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        
        stack, res = [root, ], []
        while len(stack) > 0:
            root = stack.pop()
            if root != None:
                res.append(root.val)
            for c in root.children:
                stack.append(c)
        
        return res[::-1]
        