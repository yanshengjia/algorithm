"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
Use a hash table instead of a fixed size counter. Imagine allocating a large size array to fit the entire range of unicode characters, which could go up to more than 1 million. A hash table is a more generic solution and could adapt to any range of characters.

Solution:
1. Hash Table. Anagram means the type of chars in t is the same with its in s, as well as quantity.
2. Sorting. Sort two strings, if t is an anagram of s, they will be identical.
"""


# Hash Table
# Time-O(N), because accessing the counter table is a constant time operation.
# Space-O(1), Although we do use extra space, the space complexity is O(1)O(1) because the table's size stays constant no matter how large nn is.
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = dict()
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        
        for c in t:
            if c not in d:
                return False
            else:
                d[c] -= 1
        
        for k,v in d.items():
            if v != 0:
                return False
        
        return True
        


