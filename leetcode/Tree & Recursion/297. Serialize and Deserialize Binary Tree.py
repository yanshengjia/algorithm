"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


Solution:
Preorder DFS / BFS
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Preorder DFS Recursion
# Time: O(N), N is the tree size
# Space: O(N)
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def dfs(root, string):
            # a recursive helper
            if root == None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = dfs(root.left, string)
                string = dfs(root.right, string)
            return string
        
        string = dfs(root, "")
        return string
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def construct_tree(l):
            if len(l) == 0:
                return
            else:
                val = l.pop(0)
                if val == 'None':
                    return None
                root = TreeNode(val)
                root.left = construct_tree(l)
                root.right = construct_tree(l)
            return root
        
        l = data.split(',')
        return construct_tree(l)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


# DFS Iteration + Stack
class Codec:
    def __init__(self):
        self.en = '#'
        self.sep = ','

    def serialize(self, root):
        if not root:
            return None

        res = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                res.append(str(cur.val))
                stack.append(cur)
                cur = cur.left
            else:
                res.append(self.en)
                cur = stack.pop()
                cur = cur.right
    
        return self.sep.join(res)

    def deserialize(self, data):
        if data == None:
            return None
        
        data = data.split(self.sep)
        l = len(data)

        cur = root = TreeNode(int(data[0]))
        stack = [root]
        i = 1
        while i < l:
            while i < l and data[i] != self.en:
                cur.left = TreeNode(int(data[i]))
                cur = cur.left
                stack.append(cur)
                i += 1

            while i < l and data[i] == self.en:
                cur = stack.pop()
                i += 1

            if i < l:
                cur.right = TreeNode(int(data[i]))
                cur = cur.right
                stack.append(cur)
                i += 1

        return root


# BFS Iteration + Queue
# Level Order Traversal
class Codec:
    def __init__(self):
        self.en = '#'
        self.sep = ','

    def serialize(self, root):
        if not root:
            return None

        res = [str(root.val)]
        queue = [root]
        while queue:
            node = queue.pop(0)
            for cur in [node.left, node.right]:
                if cur:
                    res.append(str(cur.val))
                    queue.append(cur)
                else:
                    res.append(self.en)
        
        string = self.sep.join(res)
        print(string)
        return string

    def deserialize(self, data):
        if data == None:
            return None
        
        data = data.split(self.sep)
        l = len(data)

        cur = root = TreeNode(int(data[0]))
        queue = [root]
        i = 1
        
        while i < l and queue:
            cur = queue.pop(0)
            if data[i] != self.en:
                cur.left = TreeNode(int(data[i]))
                queue.append(cur.left)
            i += 1
            
            if data[i] != self.en:
                cur.right = TreeNode(int(data[i]))
                queue.append(cur.right)
            i += 1
        
        return root


# BFS Iteration + Queue
# Deque
from collections import deque
class Codec:
    def __init__(self):
        self.en = '#'
        self.sep = ','

    def serialize(self, root):
        if not root:
            return None

        res = [str(root.val)]
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            for cur in [node.left, node.right]:
                if cur:
                    res.append(str(cur.val))
                    queue.append(cur)
                else:
                    res.append(self.en)
        
        string = self.sep.join(res)
        return string

    def deserialize(self, data):
        if data == None:
            return None
        
        data = data.split(self.sep)
        l = len(data)

        cur = root = TreeNode(int(data[0]))
        queue = deque()
        queue.append(root)
        i = 1
        
        while i < l and queue:
            cur = queue.popleft()
            if data[i] != self.en:
                cur.left = TreeNode(int(data[i]))
                queue.append(cur.left)
            i += 1
            
            if data[i] != self.en:
                cur.right = TreeNode(int(data[i]))
                queue.append(cur.right)
            i += 1
        
        return root