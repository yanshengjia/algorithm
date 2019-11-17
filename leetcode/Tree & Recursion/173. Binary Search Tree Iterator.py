"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.


Example:

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.


Solution:
Next node of current node is the successor of current node x in BST.
* If right(x) is not empty, successor(x) = the min in right(x), x 右子树中的最左下节点
* If right(x) is empty, go up the tree until the current node is a left child, successor(x) is the parent of the current node.


1. Output BST to array
2. Controlled Recursion with leftmost_inorder()
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Output BST to array
class BSTIterator:
    # Time: O(N), N is tree size
    # Space: O(N)
    def __init__(self, root: TreeNode):
        self.p = 0
        self.array = []
        
        cache = []
        while root or cache:
            while root:
                cache.append(root)
                root = root.left
            
            root = cache.pop()
            self.array.append(root.val)
            root = root.right
        
    # Time: O(1)
    # Space: O(1)
    def next(self) -> int:
        """
        @return the next smallest number
        """
        res = self.array[self.p]
        self.p += 1
        return res


    # Time: O(1)
    # Space: O(1)
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.p >= len(self.array):
            return False
        return True
        

# Controlled Recursion with leftmost_inorder()
class BSTIterator:
    # Time: O(H), H is the tree height, O(N) at worst case
    # Space: O(H) avg case, O(N) at worst case
    def __init__(self, root: TreeNode):
        self.stack = [] # for recursion simulation
        
        self.leftmost_inorder(root) # init the stack
    
    
    def leftmost_inorder(self, node):
        # push all elements in the leftmost branch of node to self.stack
        while node:
            self.stack.append(node)
            node = node.left
        
    # Time: O(1+h), h is the tree height of leftmost subtree of node.right
    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop() # current smallest node
        
        # if right(node) is not empty, push the leftmost branch of node.right into self.stack
        if node.right:
            self.leftmost_inorder(node.right)
        
        return node.val
        
    # Time: O(1)
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.stack) > 0:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()