# DFS: explore as deep as possible before coming back
# Time Complexity: O(N), where N is the number of nodes in the binary tree. We visit each node once.
# Space Complexity: O(H), where H is the height of the binary tree. This space is used by the recursive call stack.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        # recursively add nodes val from left to right to current level 
        def dfs(node: TreeNode, level: int):
            # before current level traversal
            if len(levels) == level:
                levels.append([])

            # add node val to current level
            if node:
                levels[level].append(node.val)

            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)
            
        dfs(root, 0)
        return levels


# BFS: explore all nodes at the current level before moving to the next level
# Time Complexity: O(N), where N is the number of nodes in the binary tree. We visit each node once.
# Space Complexity: O(W), where W is the maximum width of the binary tree. This space is used by the queue.
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        level = 0
        q = deque([root]) # double-ended queue with a single element root

        # use deque to bfs
        while q:
            # start current level by adding empty list into levels
            levels.append([])

            q_len = len(q) # all nodes will be stored in queue, use queue length to bfs next level
            
            for i in range(q_len): # scan current level
                # traverse from left to right
                node = q.popleft()
            
                levels[level].append(node.val) # store current node val to current level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            level += 1
        return levels