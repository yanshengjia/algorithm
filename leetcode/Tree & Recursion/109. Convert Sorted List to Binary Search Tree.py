"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5


Solution:
1. Convert linked list to array, build the tree recursively.

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Convert linked list to array, convert the array to BST recursively.
# Time: O(N), since we convert the linked list to an array initially and then we convert the array into a BST. Accessing the middle element now takes O(1) time and hence the time complexity comes down.
# Space: O(N), where N is the number of nodes in linked list. This is due to the array we construct initially. 
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        array = []
        while head != None:
            array.append(head.val)
            head = head.next
        
        root = self.recursion(array)
        return root

    def recursion(self, array):
        if len(array) == 0:
            return None
        mid = len(array) // 2
        root = TreeNode(array[mid])
        root.left = self.recursion(array[:mid])
        root.right = self.recursion(array[mid+1:])
        return root
        
        