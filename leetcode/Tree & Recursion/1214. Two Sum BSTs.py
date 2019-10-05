"""
Given two binary search trees, return True if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.


Example 1:
  2     1
 / \   / \
1   4 0   3

Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.


Solution:
Do an in-order traversal of each tree to convert them to sorted arrays.
Then it becomes a two sum question. Use Hashtable or Two Pointers, whatever your like.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Time: O(M+N), M is the size of tree1, N is the size of tree2
# Space: O(M+N)
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        nodes1 = self.in_order(root1)
        nodes2 = self.in_order(root2)
        
        d = dict()
        for v in nodes1:
            d[target - v] = 1
        
        for v in nodes2:
            if v in d:
                return True
        return False
    
    
    def in_order(self, root):
        if root == None:
            return []
        nodes = []
        cache = []
        while len(cache) > 0 or root:
            while root:
                cache.append(root)
                root = root.left
            
            root = cache.pop()
            nodes.append(root.val)
            root = root.right
        return nodes
