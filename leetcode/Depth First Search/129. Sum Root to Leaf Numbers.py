"""
Desc:

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.


Solution:
DFS
可以直接在 DFS 的过程中将值累加，这样节省空间。
join 只能 concat 字符串数组
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        res = []
        path = []
        self.dfs(root, path, res)
        sum = 0
        for path in res:
            num = int(''.join(str(x) for x in path))
            sum += num
        return sum
        
    def dfs(self, root, path, res):
        path.append(root.val)
        if root.left == None and root.right == None:
            res.append(copy.deepcopy(path))
        if root.left:
            self.dfs(root.left, path, res)
            path.pop()
        if root.right:
            self.dfs(root.right, path, res)
            path.pop()
