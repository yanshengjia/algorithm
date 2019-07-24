"""
Implement a Queue by linked list. Support the following basic methods:

1.enqueue(item). Put a new item in the queue.
2.dequeue(). Move the first item out of the queue, return it.


Example 1:

Input:
enqueue(1)
enqueue(2)
enqueue(3)
dequeue() // return 1
enqueue(4)
dequeue() // return 2


Solution:
做一些必要的初始化，在 MyQueue 类的 __init__() 中维护一个链表，注意在链表长度为1时 dequeue 之后需要重置 tail (此时 tail == None) 
"""


class Node:
    def __init__(self, _val):
        self.val = _val
        self.next = None


class MyQueue:
    def __init__(self):
        self.head = Node(0)
        self.tail = self.head
        self.size = 0
    """
    @param: item: An integer
    @return: nothing
    """
    def enqueue(self, item):
        # write your code here
        node = Node(item)
        self.tail.next = node
        self.tail = self.tail.next
        self.size += 1

    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        if self.size < 1:
            return None
        res = self.head.next.val
        self.head.next = self.head.next.next
        self.size -= 1
        if self.size == 0:
            self.tail = self.head  # self.tail == None, need to reset
        return res
