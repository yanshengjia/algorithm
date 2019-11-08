"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3


Solution:
BST Inorder -> Ascending array
swap two mistake elements in an ascending array
* Recurison
* Interative
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Iteration
# Time: O(n), n is the tree size
# Space: O(h), tree height
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = None
        wrong_node_1, wrong_node_2 = None, None
        
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and pre.val > root.val:
                wrong_node_2 = root
                if wrong_node_1 == None:    # find the first mistake node
                    wrong_node_1 = pre
                else:   # find the second mistake node
                    break
            pre = root
            root = root.right
        
        wrong_node_1.val, wrong_node_2.val =  wrong_node_2.val, wrong_node_1.val
        