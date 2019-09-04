"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

Solution:
Use a Hashtable to record the frequency of each characters.
Scan twice. First round to build the hashtable, second round to find the first unique char.
"""


# Linear time solution
# Time: O(N), where N is the length of s, since we have to go through the string two times.
# Space: O(N), since we have to keep a hash map with N elements.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for c in s:
            d[c] = d.get(c, 0) + 1
        
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
        