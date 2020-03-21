"""
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.


Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

Example 3:
Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]

Example 4:
Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]

Example 5:
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]


Solution:
1. Two inorder traversal, sort, log time complexity
2. Iterative inorder traversal, one pass, linear time
Do iterative inorder traversal of both trees in parallel.
At each step add the smallest available value in the output.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Two inorder traversal, sort
# Time: O((M+N)log(M+N)), where M and N are node numbers
# Space: O(M+N)
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1 = self.inorder(root1)
        l2 = self.inorder(root2)
        l1.extend(l2)
        return sorted(l1)
    
    
    def inorder(self, root: TreeNode):
        res = []
        stack = []
        
        while root or len(stack) > 0:
            while root:
                stack.append(root)
                root = root.left
        
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


# One pass inorder traversal, no sort
# Time: O(M+N)
# Space: O(M+N)
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        stack1, stack2 = [], []
        
        # traverse two trees parallelly
        while root1 or root2 or stack1 or stack2:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left
            
            # add the smaller value into res
            if not stack2 or stack1 and stack1[-1].val <= stack2[-1].val:
                root1 = stack1.pop()
                res.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                res.append(root2.val)
                root2 = root2.right
        return res     
