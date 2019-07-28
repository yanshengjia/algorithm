"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example1

Input: 
{1,3,2,5}
{2,1,3,#,4,#,7}
Output:
{3,4,5,5,4,#,7}
Explanation:
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  

Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7


Solution:
recursion
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
    @param t1: the root of the first tree
    @param t2: the root of the second tree
    @return: the new binary tree after merge
    """
    def mergeTrees(self, t1, t2):
        # Write your code here
        if t1 is None and t2 is None:
            return None
        elif t1 is None and t2 is not None:
            return t2
        elif t1 is not None and t2 is None:
            return t1
        else:
            res = TreeNode(t1.val + t2.val)
            res.left = self.mergeTrees(t1.left, t2.left)
            res.right = self.mergeTrees(t1. right, t2.right)
        return res
