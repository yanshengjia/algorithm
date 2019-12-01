"""
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4


Solution:
DFS Recursion Postorder Traversal
Execute self.is_uni() first, otherwise in the if statement, it may not be executed.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Time: O(N), since we visited each node once
# Due to the algorithm's depth-first nature, the is_uni status of each node is computed from bottom up. When given the is_uni status of its children, computing the is_uni status of a node occurs in O(1)O(1) This gives us O(1) time for each node in the tree with O(N) total nodes for a time complexity of O(N)
# Space: O(H), H is the height of tree. Each recursive call of is_uni requires stack space. Since we fully process is_uni(node.left) before calling is_uni(node.right), the recursive stack is bound by the longest path from the root to a leaf - in other words the height of the tree.
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.count = 0
        self.is_uni(root)
        return self.count
    
    def is_uni(self, root):
        # leaf node
        if root.left == None and root.right == None:
            self.count += 1
            return True
        
        # recursively call
        is_uni_flag = True
        if root.left:
            if self.is_uni(root.left) and root.val == root.left.val and is_uni_flag:
                is_uni_flag = True
            else:
                is_uni_flag = False
        
        if root.right:
            if self.is_uni(root.right) and root.val == root.right.val and is_uni_flag:
                is_uni_flag = True
            else:
                is_uni_flag = False
        
        if is_uni_flag:
            self.count += 1
        
        return is_uni_flag
        