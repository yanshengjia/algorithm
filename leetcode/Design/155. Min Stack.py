"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.


Solution:
1. Use a list [(val, cur_min)]
Update the cur_min when a element is pushed and keep all the previous cur_min
2. heapq
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []  # [(val, cur_min)]
        
    def push(self, x: int) -> None:
        cur_min = self.getMin()
        if cur_min == None or x < cur_min:
            cur_min = x
        self.stack.append((x, cur_min))

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][1]
        else:
            return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()