"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:

   1
  /|\ 
 3 2 4
/ \
5 6

We should return its max depth, which is 3.


Solution: 
1. Recursion, take care of the case that node has no child
2. Iteration, store the cur depth with the node
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# Recursion
# Time: O(N), where N is the tree size
# Space: O(H), where H is the tree height, H = logN
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        elif len(root.children) == 0:
            return 1
        return max([self.maxDepth(child) for child in root.children]) + 1


# Iteration
# Time: O(N)
# Space: O(N)
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        stack = [(root, 1)]
        max_depth = 0

        while len(stack) > 0:
            node, cur_dpeth = stack.pop()
            max_depth = max(max_depth, cur_dpeth)
            for c in node.children:
                stack.append((c, cur_dpeth + 1))
        return max_depth

