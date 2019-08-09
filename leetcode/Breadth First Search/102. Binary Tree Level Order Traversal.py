"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]


Solution:
1. DFS Recursion
2. BFS + Stack/Queue Iteration

The zero level contains only one node root. The algorithm is simple :
    Initiate queue with a root and start from the level number 0 : level = 0.

    While queue is not empty :
    * Start the current level by adding an empty list into output structure levels.
    * Compute how many elements should be on the current level : it's a queue length.
    * Pop out all these elements from the queue and add them into the current level.
    * Push their child nodes into the queue for the next level.
    * Go to the next level level++.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# DFS Recursion
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return levels

# BFS + Stack
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = [[root.val]]
        stack = [root]
        next_level = []
        next_level_val = []
        while len(stack) > 0:
            node = stack.pop(0)
            if node.left != None:
                next_level.append(node.left)
                next_level_val.append(node.left.val)
            if node.right != None:
                next_level.append(node.right)
                next_level_val.append(node.right.val)
            if len(stack) == 0:
                if len(next_level_val) > 0:
                    res.append(next_level_val)
                stack = next_level
                next_level = []
                next_level_val = []
        return res


# BFS + Stack
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        if root == None:
            return []
        res = []
        level = [root]
        res.append([root.val])
        while len(level) > 0:
            cache_node = []
            cache_value = []
            for i in range(len(level)):
                node = level.pop(0)
                if node.left != None:
                    cache_node.append(node.left)
                    cache_value.append(node.left.val)
                if node.right != None:
                    cache_node.append(node.right)
                    cache_value.append(node.right.val)
            if len(cache_node) > 0:
                level = cache_node
                res.append(cache_value)
        return res


# BFS + Queue
# Time-O(N), since each node is processed exactly once.
# Space-O(N) to keep the output structure which contains N node values.
from collections import deque
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        level = 0
        queue = deque([root,])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level 
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)
                
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # go to next level
            level += 1
        
        return levels