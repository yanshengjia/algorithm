"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:

   1
  /|\
 3 2 4
/ \
5  6

Return its preorder traversal as: [1,3,5,6,2,4].

Follow up:
Recursive solution is trivial, could you do it iteratively?


Solution:
1. Recursion
2. Iterative + Stack
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


# Recursion
# Time: O(N), where N is the size of tree
# Space: O(N)
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.dfs(root, res)
        return res
    
    def dfs(self, root, res):
        if root == None:
            return
        res.append(root.val)
        for c in root.children:
            self.dfs(c, res)



# Iterative
# Time: O(N), > 23%, where N is the size of tree
# Space: O(N)
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        
        stack, res = [root, ], []
        while len(stack) > 0:
            root = stack.pop()
            if root != None:
                res.append(root.val)
            for c in reversed(root.children):
                stack.append(c)
            # stack.extend(root.children[::-1])
        return res    
        