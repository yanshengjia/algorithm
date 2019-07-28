"""
Given a binary search tree and a range [k1, k2], return node values within a given range in ascending order.

Example 1:

Input：{5},6,10
Output：[]
        5
it will be serialized {5}
No number between 6 and 10


Solution:
1. recursion: dfs with tree pruning
2. inorder traversal BST to get an ascending array
"""


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# recursion
class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        nums = []
        self.dfs(root, k1, k2, nums)
        return sorted(nums)
    
    def dfs(self, root, k1, k2, nums):
        if root:
            if k1 <= root.val <= k2:
                nums.append(root.val)
                self.dfs(root.left, k1, k2, nums)
                self.dfs(root.right, k1, k2, nums)
            elif root.val > k2:
                self.dfs(root.left, k1, k2, nums)
            else:
                self.dfs(root.right, k1, k2, nums)
