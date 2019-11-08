"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]


Solution:
BFS + Hashmap

store the col index of each node when traversal
use a dict to collect nodes of same column
sort the res list before return.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# BFS + Hashmap
# Time: O(n), n is the tree size
# Space: O(n), worst case
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        d = dict()  # {col_idx: [node_val]}
        queue = [(root, 0)] # (node, col_index)
        while queue:
            node, col_idx = queue.pop(0)
            if node:
                if col_idx not in d:
                    d[col_idx] = [node.val]
                else:
                    d[col_idx].append(node.val)

                queue.append((node.left, col_idx - 1))
                queue.append((node.right, col_idx + 1))
        
        sorted_d = sorted(d.items())
        res = [i[1] for i in sorted_d]
        return res
