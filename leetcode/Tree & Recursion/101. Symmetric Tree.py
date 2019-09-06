"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up:
Bonus points if you could solve it both recursively and iteratively.


Solution:
1. Recursion
2. Iteration
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursion
# Time: O(N), where N is the size of tree
# Space: The number of recursive calls is bound by the height of the tree. In the worst case, the tree is linear and the height is in O(n). Therefore, space complexity due to recursive calls on the stack is O(n) in the worst case.
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)
    
    def isMirror(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val == root2.val:
            return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)
        else:
            return False
        

# Iterative
# Time: O(N), Because we traverse the entire input tree once, the total run time is O(N), where nn is the total number of nodes in the tree.
# Space: There is additional space required for the search queue. In the worst case, we have to insert O(N) nodes in the queue. Therefore, space complexity is O(N).
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        stack1, stack2 = [root], [root]
        while stack1 and stack2:
            root1 = stack1.pop()
            root2 = stack2.pop()
            
            if root1 == None and root2 == None:
                continue
            if root1 == None or root2 == None:
                return False
            
            if root1.val != root2.val:
                return False
            else:
                stack1.append(root1.left)
                stack2.append(root2.right)
                stack1.append(root1.right)
                stack2.append(root2.left)
        return True
