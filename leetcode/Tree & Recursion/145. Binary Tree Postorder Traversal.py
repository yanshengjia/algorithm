"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.


Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [2,1]

Example 5:
Input: root = [1,null,2]
Output: [2,1]


Solution:
* Recursion
* Iterative Postorder Traversal
    * push nodes into stacks: right - root - left, root = root.left, search towards left subtree
    * when popping from stack, consider 2 conditions: 
        (1) right subtree not processed, search towards right subtree and keep the root info in stack for future use (stack[-1] = root) 
        (2) on the leftmost leaf, add it to res
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursion
# Time: O(N), N = tree size
# Space: O(N) in worst case, max recursion stack
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def postorderTraversalHelper(node):
            if node == None:
                return
            postorderTraversalHelper(node.left)
            postorderTraversalHelper(node.right)
            res.append(node.val)
        
        postorderTraversalHelper(root)
        return res


# Iteration
# Time: O(N)
# Space: O(N) in worst case skewed tree. In average case, O(H) to keep the stack, H is the tree height
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        s = []
        
        while root != None or len(s) > 0:
            # push nodes to stack: right -> root -> left
            while root != None:
                if root.right:
                    s.append(root.right)
                s.append(root)
                root = root.left
            
            root = s.pop()
            
            # if the right subtree is not yet processed
            if s and s[-1] == root.right:
                s[-1] = root
                root = root.right
            else:
                # if we are on the leftmost leaf
                res.append(root.val)
                root = None
        return res
        
