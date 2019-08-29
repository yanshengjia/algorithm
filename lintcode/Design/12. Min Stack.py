"""
Implement a stack with following functions:
* push(val) push val into the stack
* pop() pop the top element and return it
* min() return the smallest number in the stack
All above should be in O(1) cost.


Example 1:

Input:
  push(1)
  pop()
  push(2)
  push(3)
  min()
  push(1)
  min()
Output:
  1
  2
  1


Solution:
The point is that we should maintain a structure which can record min number everytime we push a number.
stack [(number, current_min)]
"""


# O(1) for push(), pop(), min()
class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        if len(self.stack) == 0:
            m = number
            self.stack.append((number, m))
        else:
            m = self.min()
            if number < m:
                m = number
            self.stack.append((number, m))

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        return self.stack.pop(-1)[0]

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        return self.stack[-1][1]
