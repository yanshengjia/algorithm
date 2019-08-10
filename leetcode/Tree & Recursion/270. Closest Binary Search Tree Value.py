"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4


Solution:
1. Recursive Inorder + Linear search, O(N) time
2. Iterative Inorder, O(k) time
3. Binary Search, O(H) time
"""


# Recursive Inorder + Linear search, O(N) time
# Time complexity : O(N) because to build inorder traversal and then to perform linear search takes linear time.
# Space complexity : O(N) to keep inorder traversal. 
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        return min(inorder(root), key = lambda x: abs(target - x))


# Iterative Inorder, O(k) time
# Time complexity : O(k) in the average case and O(H+k) in the worst case, where k is an index of closest element. It's known that average case is a balanced tree, in that case stack always contains a few elements, and hence one does 2k2k operations to go to kth element in inorder traversal (k times to push into stack and then k times to pop out of stack). That results in O(k) time complexity. The worst case is a completely unbalanced tree, then you first push H elements into stack and then pop out k elements, that results in O(H+k) time complexity.
# Space complexity : up to O(H) to keep the stack in the case of non-balanced tree. 
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack, pred = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            if pred <= target and target < root.val:
                return min(pred, root.val, key = lambda x: abs(target - x))
                
            pred = root.val
            root = root.right

        return pred


# Binary Search
# Time: O(H) since here one goes from root down to a leaf.
# Space: O(1)
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest


# Binary Search
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        min = float('inf')
        self.closest = root.val
        self.dfs(root, target, min)
        return self.closest
    
    def dfs(self, root, target, min):
        if root:
            if abs(root.val - target) < min:
                min = abs(root.val - target)
                self.closest = root.val
            if root.val > target:
                self.dfs(root.left, target, min)
            else:
                self.dfs(root.right, target, min)