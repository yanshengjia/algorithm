"""
Given a binary tree, return all root-to-leaf paths.

Example 1:

Input：{1,2,3,#,5}
Output：["1->2->5","1->3"]
Explanation：
   1
 /   \
2     3
 \
  5


Solution:
DFS + Backtracking
"""


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        res, path = [], []
        self.dfs(root, path, res)
        return res
    
    def dfs(self, root, path, res):
        if root == None:
            return
        path.append(root.val)
        if root.left == None and root.right == None:
            path = [str(i) for i in path]
            res.append('->'.join(path))
        if root.left:
            self.dfs(root.left, path, res)
            path.pop()  # backtracking
        if root.right:
            self.dfs(root.right, path, res)
            path.pop()  # backtracking
