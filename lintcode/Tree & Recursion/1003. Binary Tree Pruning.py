"""
Given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return this tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:

Input: {1,#,0,0,1}
Output: {1,#,0,#,1}
Explanation: 
  Only the red nodes satisfy the property "every subtree not containing a 1".
  The diagram on the right represents the answer.


Solution:
DFS
If the val of leaf node is 0, delete it and return None.
当一个节点已经删除了，返回上层栈时，此时，原来的父节点也是叶子节点了，相同的删除结点判断条件。
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# Time-O(N), where N is the number of nodes in the tree
# Space-O(H), where H is the height of the tree. This represents the size of the implicit call stack in our recursion.
class Solution:
    """
    @param root: the root
    @return: the same tree where every subtree (of the given tree) not containing a 1 has been removed
    """
    def pruneTree(self, root):
        # Write your code here
        if root == None:
            return root
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and root.left == None and root.right == None:
            return None
        else:
            return root
