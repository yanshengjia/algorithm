"""
Description:
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
Given binary search tree: root = {6,2,8,0,4,7,9,#,#,3,5}


Solution:
Recursion
利用 BST 的性质，左<根<右，判断根结点与 p q 的大小关系，做一些剪枝。
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
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
        # write your code here
        mn, mx = min(p.val, q.val), max(p.val, q.val)
        if mn <= root.val <= mx:
            return root
        else:
            if root.val > mx:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.right, p, q)
            
        