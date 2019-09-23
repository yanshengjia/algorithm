"""
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:

   1
  /|\
 3 2 4
/\
5 6

We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]


Solution:
BFS + Queue
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


# BFS
# Time: O(N), N is the tree size
# Space: O(N)
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = [[root.val]]
        pre_level = [root]
        cur_level = []
        cur_level_val = []
        
        while len(pre_level) > 0 or len(cur_level) > 0:
            while pre_level:
                node = pre_level.pop(0)
                for c in node.children:
                    cur_level_val.append(c.val)
                    cur_level.append(c)
            if len(cur_level) > 0:
                pre_level = cur_level
                res.append(cur_level_val)
                cur_level = []
                cur_level_val = []
        return res
