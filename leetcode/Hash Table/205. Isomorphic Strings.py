"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true


Solution:
Hash Table, store each mapping
"""


# Hashtable
# Time: O(N), >80%, where N is the length of s
# Space: O(N)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        if ls != lt:
            return False
        d, vals = dict(), set()
        for i in range(ls):
            cs, ct = s[i], t[i]
            if cs not in d:
                d[cs] = ct
                if ct in vals:
                    return False
                vals.add(ct)
            else:
                if ct != d[cs]:
                    return False
        return True