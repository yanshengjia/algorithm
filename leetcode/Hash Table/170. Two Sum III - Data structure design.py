"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false


Solution:
Hashtable
store each number as key and the time of occurrence of number as value
"""


# Hash Table
# Time: O(1) for add(), O(N) for find(), where N is the length of hashtable.keys()
# Space: O(N)
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = dict()

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.table[number] = self.table.get(number, 0) + 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i in self.table.keys():
            j = value - i
            if j in self.table and (i != j or self.table.get(i) > 1):
                return True
        return False
                    
                    
                    

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)