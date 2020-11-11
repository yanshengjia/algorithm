"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.


Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.


Constraints:
* The number of nodes in the binary tree is in the range [1, 10^5].
* Each node's value is between [-10^4, 10^4].


Solution:
Recursion DFS
Record the maximum value along the path from the root to the node.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursion DFS
# Time: O(N), N is tree size
# Space: O(H), H is tree height, recursion stack
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0
        
        def dfs(node, max_val):
            if node == None:
                return
            
            dfs(node.left, max(max_val, node.val))
            dfs(node.right, max(max_val, node.val))
            
            if node.val >= max_val:
                self.cnt += 1
            
        dfs(root, -99999)
        return self.cnt
        

# Recursion DFS
# Time: O(N), N is tree size
# Space: O(H), H is tree height, recursion stack
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_val):
            if node == None:
                return 0
            res = 1 if node.val >= max_val else 0
            return dfs(node.left, max(max_val, node.val)) + dfs(node.right, max(max_val, node.val)) + res
            
        return dfs(root, -99999)
