"""
Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.

 

Example:

Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false


Solution:
Exclude all empty vector
next(): return cur value, move the iterator forward
hasNext(): back to pre value
"""


class Vector2D:

    def __init__(self, v: List[List[int]]):
        # remove none vector
        self.v = []
        for arr in v:
            if len(arr) > 0:
                self.v.append(arr)

        self.row = 0
        self.col = 0

    # Time: O(1)
    def next(self) -> int:
        res = self.v[self.row][self.col]
        
        if self.col < len(self.v[self.row]) - 1:
            self.col += 1
        else:
            self.row += 1
            self.col = 0
        return res

    # Time: O(1)
    def hasNext(self) -> bool:
        # back to pre one
        if self.col > 0:
            col = self.col - 1
            row = self.row
        else:
            if self.row > 0:
                row = self.row - 1
                col = len(self.v[row]) - 1
            else:
                row = -1
                col = 0
        
        if len(self.v) == 0:
            return False
        if row >= len(self.v) - 1 and col >= len(self.v[row]) - 1:
            return False
        return True


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()