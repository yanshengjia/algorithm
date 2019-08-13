"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();


Solution:
1. List + Dict
Keep track of the index of the added elements, so when we remove them, we copy the last one into it. Meanwhile update the position value of last one in dict.
From Python docs (https://wiki.python.org/moin/TimeComplexity) we know that list.append() takes O(1), both average and amortized. Dictionary get and set functions take O(1) average, so we are OK.

"""


import random

# List + Dict
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []  # keep vals
        self.d = {}  # keep the position of vals, {val: the index of val in self.l}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.d:
            self.l.append(val)  # O(1)
            self.d[val] = len(self.l) - 1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.d:
            if val == self.l[-1]:
                self.l.pop()
            else:
                last = self.l.pop()  # O(1), remove last element of self.l, and put the val of last to the position of 'val'
                pop_index = self.d[val]
                self.l[pop_index] = last
                self.d[last] = pop_index
            self.d.pop(val)  # O(1)
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.l[random.randint(0, len(self.l)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()