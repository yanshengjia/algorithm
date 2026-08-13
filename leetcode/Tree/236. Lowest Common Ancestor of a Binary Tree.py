# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursive postorder DFS
# - Return a node immediately if it is p or q.
# - Recursively search both children.
# - If each side returns a node, the current node is their LCA.
# - Otherwise propagate the non-null result upward.
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree (due to recursion stack).
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # An empty subtree contains neither p nor q.
        if not root:
            return None

        # If this node is one of the targets, return it to its parent call.
        # A node is allowed to be an ancestor of itself.
        if root == p or root == q:
            return root

        # Search the left subtree for p, q, or an LCA already found below.
        left = self.lowestCommonAncestor(root.left, p, q)

        # Search the right subtree for p, q, or an LCA already found below.
        right = self.lowestCommonAncestor(root.right, p, q)

        # p and q were found in different subtrees, so root is their first
        # (and therefore lowest) common ancestor.
        if left and right:
            return root

        # Only one subtree found a target or an LCA; pass that result upward.
        return left if left else right


# Iterative approach using parent pointers 
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(n), for storing parent pointers and the stack.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root is None:
            return None
        
        stack = [root] # for bfs
        parents = {root: None} # store parent pointers for each node

        # don't have to bfs the whole tree, iterate until we find both p and q
        while p not in parents or q not in parents:
            node = stack.pop()

            if node.left:
                stack.append(node.left)
                parents[node.left] = node
            if node.right:
                stack.append(node.right)
                parents[node.right] = node
        
        # since we have all the parent points, we can backtrack from p and q to find LCA
        ancestors = set() # ancestors set() for node p

        # backtrack from p, find all ancestors of p
        while p:
            ancestors.add(p)
            p = parents[p]
        
        # backtrack from q, the first ancestor of q which is also in q's ancestor set is their LCA
        while q not in ancestors:
            q = parents[q]
        return q
