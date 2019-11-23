"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4


Solution:
LRU Cache: a cache replacement policy, decides which item we should evict when cache reaches its capacity. Evict the least recently used item.
https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU

1. OrderedDict
* move_to_end(key, last=True): move an existing key to right end of an ordered dictionary
* popitem(last=True): returns and removes a (key, value) pair. The pairs are returned in LIFO order if last is true or FIFO order if false

Python OrderedDict: key-value pairs ordered based on their insertion sequence, kind of like appending items to a list
https://docs.python.org/3/library/collections.html#collections.OrderedDict


2. Hashmap + DoubleLinkedList
This problem can be solved with a hashmap that keep track of the keys and its value in the double linked list.
https://leetcode.com/problems/lru-cache/solution/ 
用双向链表连接 Hashmap 中的 key-value pair，维护链表的节点从最近访问到最旧访问的顺序。
keep track of head node and tail node. 这两个结点是工具人，the nodes in between are ordered based on time which they are accessed, from head to tail, most recently to least recently.
实现 OrderedDict 中的 move_to_end() 和 popitem()，在实际实现中实现的是 move_to_head() 和 pop_tail()，因为实现简单。


Why hashmap? O(1) put and get
Why double linkedlist? O(1) remove node, add node, move_to_end(), pop_head()
Why we need head and tail in DLinkedList? Mark the boundary, so we don't need to check the NULL node during the update.
"""


# OrderedDict
# Space: O(capacity)
from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # self is a OrderedDict object, key-value pairs ordered by insertion sequence
        self.capacity = capacity

    # Time: O(1)
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return -1
        
        self.move_to_end(key) # move an existing key to right end of an ordered dictionary
        return self[key]
        
    # Time: O(1)
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            # evict the least recently used item, i.e. the item at head (left end) of OrderedDict
            self.popitem(last = False)    # returns and removes a (key, value) pair. The pairs are returned in LIFO order if last is true or FIFO order if false.
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class DLinkedNode():
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


# Space: O(capacity) 
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        
        self.head.next = self.tail
        self.tail.pre = self.head
    
    def add_node(self, node):
        # add the new node right after head
        node.pre = self.head
        node.next = self.head.next
        
        self.head.next.pre = node
        self.head.next = node

    
    def remove_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        
    
    def move_to_head(self, node):
        # move cur node right after head, most recently used item
        self.remove_node(node)
        self.add_node(node)
    
    def pop_tail(self):
        # evict the node left before tail, least recently used item
        lru_node = self.tail.pre
        self.remove_node(lru_node)
        return lru_node
    
    # Time: O(1)
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_head(node)     # most recently used node
            # print('get: ' + str(key))
            # self.print_dlinkedlist()
            return node.value
        else:
            return -1
    
    # Time: O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            new_node = DLinkedNode(key, value)
            self.add_node(new_node)
            self.cache[key] = new_node
            self.size += 1
            
            if self.size > self.capacity:
                # evict the lru node, delete key-value pair in hashmap
                tail = self.pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        
        # print('put: ({},{})'.format(key, value))
        # self.print_dlinkedlist()
    
    def print_dlinkedlist(self):
        dlinkedlist = []
        tmp = DLinkedNode(0, 0)
        tmp.next = self.head
        while tmp.next:
            dlinkedlist.append("{}:{}".format(tmp.key, tmp.value))
            tmp = tmp.next
        print("->".join(dlinkedlist))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)       # returns 1
    cache.put(3, 3)    # evicts key 2
    cache.get(2)       # returns -1 (not found)
    cache.put(4, 4)    # evicts key 1
    cache.get(1)       # returns -1 (not found)
    cache.get(3)       # returns 3
    cache.get(4)   