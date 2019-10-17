"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

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


Solution:
1. Recursion (in place)
Flatten the left subtree of root, then set it as the right child of root (need to store the previous right child of root).
Then set the previous right child of root as the right child of the rightmost node of the flattened left subtree.
Make left subtree of root to None

2. Preorder Traversal (Not in place)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursion
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                self.flatten(root.left)
                left_tail = root.left
                while left_tail.right:
                    left_tail = left_tail.right
                right_head = root.right
                root.right = root.left
                root.left = None
                left_tail.right = right_head
            root = root.right


# Preorder Traversal
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return root
        
        nodes = []
        stack = []
        dummy = root
        
        # preorder
        while stack or dummy:
            while dummy != None:
                stack.append(dummy)
                nodes.append(dummy.val)
                dummy = dummy.left
            
            dummy = stack.pop()
            dummy = dummy.right
        
        root.left = None
        cur = root
        for i in range(1, len(nodes)):
            node = TreeNode(nodes[i])
            cur.right = node
            cur = cur.right