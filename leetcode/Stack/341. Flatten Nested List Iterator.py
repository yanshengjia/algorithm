"""
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].


Solution:
1. Flat the nesteslist recursively and store integers in a list
Pro: intuitive
Con: it copys the data, more space cose

2. Stack
Pro: real iterator, no data duplication
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


# Flat recursively
# Time: 
#   constructor: O(N)
#   next(): O(1)
#   hasNext: O(1)
# Space: O(N), where N is the number of integers in the nestedList
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.l = self.flat(nestedList)
        self.size = len(self.l)
        self.index = 0
    
    def flat(self, nestedList):
        l = []
        for ele in nestedList:
            if ele.isInteger() ==  False:
                l.extend(self.flat(ele.getList()))
            else:
                l.append(ele.getInteger())
        return l

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            self.index += 1
            return self.l[self.index - 1]
        else:
            return None
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index < self.size:
            return True
        else:
            return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


# Stack
from collections import deque
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = deque([])
        self.stack.append(nestedList)
        self.value = None

    def next(self):
        """
        :rtype: int
        """
        ret = self.value
        self.value = None
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.value:
            return True
        
        stack = self.stack
        while stack:
            top = stack.popleft()
            if len(top) == 1:
                if top[0].isInteger():
                    self.value = top[0].getInteger()
                    return True
                else:
                    stack.appendleft(top[0].getList())
            else:
                for ni in reversed(top):    # scan reversely
                    stack.appendleft([ni])
        return False