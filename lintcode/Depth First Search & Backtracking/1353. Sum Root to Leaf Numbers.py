"""
Description:
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Example:

Input: {1,2,3}
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
用一个变量 prev 来存储之前遍历到的路径上的和
sum = root.val + prev * 10
"""


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import copy

class Solution:
    """
    @param root: the root of the tree
    @return: the total sum of all root-to-leaf numbers
    """
    def sumNumbers(self, root):
        # write your code here
        res = 0
        return self.dfs(root, res)
        
    def dfs(self, root, prev):
        if root == None:
            return 0
        sum = root.val + prev * 10
        if root.left == None and root.right == None:
            return sum
        return self.dfs(root.left, sum) + self.dfs(root.right, sum)
