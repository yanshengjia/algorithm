"""
Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  


Solution:
1. Inorder Traversal, Store and Rebuild
2. Inorder Traversal with Relinking
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Inorder Traversal with Relinking
# Time: O(N), >70%, where N is the tree size
# Space: O(H), where H is the height of tree
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        
        dummy = TreeNode(-1)
        res = dummy
        
        # inorder traversal
        cache = []
        while root or len(cache) > 0:
            while root != None:
                cache.append(root)
                root = root.left
            root = cache.pop()
            root.left = None
            
            # relink
            dummy.right = root
            dummy = dummy.right
            
            root = root.right
        return res.right
