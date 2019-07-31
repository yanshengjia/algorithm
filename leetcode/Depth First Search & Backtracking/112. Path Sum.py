"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


Solution:
1. dfs + recursion
2. bfs + stack
So we start from a stack which contains the root node and the corresponding remaining sum which is sum - root.val. Then we proceed to the iterations: pop the current node out of the stack and return True if the remaining sum is 0 and we're on the leaf node. If the remaining sum is not zero or we're not on the leaf yet then we push the child nodes and corresponding remaining sums into stack.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS + Recursion
# Time-O(N), where N is the number of nodes in the tree
# Space-worst O(N), best O(logN)
# Space complexity : in the worst case, the tree is completely unbalanced, e.g. each node has only one child node, the recursion call would occur NN times (the height of the tree), therefore the storage to keep the call stack would be \mathcal{O}(N)O(N). But in the best case (the tree is completely balanced), the height of the tree would be \log(N)log(N). Therefore, the space complexity in this case would be \mathcal{O}(\log(N))O(log(N)). 
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        if root.val == sum and root.left == None and root.right == None:
            return True
        else:
            left = self.hasPathSum(root.left, sum - root.val)
            right = self.hasPathSum(root.right, sum - root.val)
            if left or right:
                return True
            else:
                return False


# BFS + Stack
# Use stack to store each node's condition, [node, remaining value], updating the remaining sum to cumulate at each visit.
# Time - O(N)
# Space - [O(logN), O(N)] 
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        de = [(root, sum - root.val), ]
        while len(de) > 0:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:  
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False
