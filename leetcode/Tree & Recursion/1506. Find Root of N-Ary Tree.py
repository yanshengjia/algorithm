"""
You are given all the nodes of an N-ary tree as an array of Node objects, where each node has a unique value.

Return the root of the N-ary tree.

Custom testing:

An N-ary tree can be serialized as represented in its level order traversal where each group of children is separated by the null value (see examples).


For example, the above tree is serialized as [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].

The testing will be done in the following way:
* The input data should be provided as a serialization of the tree.
* The driver code will construct the tree from the serialized input data and put each Node object into an array in an arbitrary order.
* The driver code will pass the array to findRoot, and your function should find and return the root Node object in the array.
* The driver code will take the returned Node object and serialize it. If the serialized value and the input data are the same, the test passes.


Example 1:
Input: tree = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]
Explanation: The tree from the input data is shown above.
The driver code creates the tree and gives findRoot the Node objects in an arbitrary order.
For example, the passed array could be [Node(5),Node(4),Node(3),Node(6),Node(2),Node(1)] or [Node(2),Node(6),Node(1),Node(3),Node(5),Node(4)].
The findRoot function should return the root Node(1), and the driver code will serialize it and compare with the input data.
The input data and serialized Node(1) are the same, so the test passes.

Example 2:
Input: tree = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
 

Constraints:
* The total number of nodes is between [1, 5 * 104].
* Each node has a unique value.

Follow up:
Could you solve this problem in constant space complexity with a linear time algorithm?


Solution:
1. Find the node with in_degree = 0

2. YOLO (You Only Look Once)
If we visit all the nodes and all the child nodes, 
then the root node would be the only node that we visit once and once only. 
The rest of the nodes would be visited twice.
Transform this problem into:
Given a list of numbers where some of the numbers appear twice, we are asked to find the number that appear only once.
Use a value_sum variable, add parent nodes' value to value_sum, deduct child nodes' value to value_sum.
Since the root node is only visited once, then the final value_sum is the value of root node.
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


# root node with in_degree = 0
# TC: O(N), N = size of tree
# SC: O(N)
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        # a set that contains all the child nodes
        seen = set()
        
        # add all the child nodes into the set
        for node in tree:
            for child in node.children:
                # either add the value or the node itself
                # since each node has unique value, adding the vaule will save some space
                seen.add(child)
        
        for node in tree:
            if node not in seen:
                return node
        

# YOLO
# TC: O(N), N is the number of nodes in tree
# SC: O(1)
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        # a set that contains all the child nodes
        value_sum = 0
        
        for node in tree:
            # the value is added as a parent node
            value_sum += node.val
            for child in node.children:
                # the value is deducted as a child node.
                value_sum -= child.val
        
        # the value of the root node is `value_sum`
        for node in tree:
            if node.val == value_sum:
                return node
