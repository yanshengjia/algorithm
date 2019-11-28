"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7


Solution:
postorder 最后一个元素是 root
root 在 inorder 中的下标用来分割左右子树
build rigth subtree first
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursion
# Time: O(N^2)
# Space: O(N)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        
        root_val = postorder.pop()
        root = TreeNode(root_val)
        root_idx = inorder.index(root_val)
        
        # build the right subtree first since its postorder
        # postorder traversal goes 'Left-Right-Parent'. And, postorder.pop() keeps picking the right-most element of the list, that means it should go 'Parent-(one of parents of) Right (subtree) - Left'.
        root.right = self.buildTree(inorder[root_idx+1:], postorder)
        root.left = self.buildTree(inorder[:root_idx], postorder)
    
        return root


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        
        root_val = postorder.pop()
        root = TreeNode(root_val)
        root_idx = inorder.index(root_val)
        
        root.left = self.buildTree(inorder[:root_idx], postorder[:root_idx])
        root.right = self.buildTree(inorder[root_idx+1:], postorder[root_idx:])
    
        return root
        

# Hashtable + Recursion
# Time: O(N)
# Space: O(N)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_map = dict()
        
        # record the index of root nodes
        for i, v in enumerate(inorder):
            inorder_map[v] = i
        
        def recursive(left, right):
            if left > right:
                return None
            
            root_val = postorder.pop()
            root_idx = inorder_map[root_val]
            root = TreeNode(root_val)
            root.right = recursive(root_idx+1, right)
            root.left = recursive(left, root_idx-1)
            return root
    
        return recursive(0, len(inorder)-1)