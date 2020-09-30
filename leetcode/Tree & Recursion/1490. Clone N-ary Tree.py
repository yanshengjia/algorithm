"""
Given a root of an N-ary tree, return a deep copy (clone) of the tree.

Each node in the n-ary tree contains a val (int) and a list (List[Node]) of its children.

class Node {
    public int val;
    public List<Node> children;
}
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Follow up: Can your solution work for the graph problem?


Solution:
* DFS
    * Recursion
    * Iterative
* BFS
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


# DFS Recursion
# Time: O(N), where N is the tree size
# Space: O(N), recursion strack
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        new_root = Node(root.val)
        for child in root.children:
            new_root.children.append(self.cloneTree(child))
        return new_root

