"""
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.


Solution:
Consider the difference of lengths of two strings. Case study.
Scan the shorter string, otherwise will have out-of-index exception.
"""


# One Pass
# Time: O(N), N is the length of s
# Space: O(1)
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        if ls > lt:
            # 1st str has shorter length
            return self.isOneEditDistance(t, s)
        
        if ls == 0 and lt == 1:
            return True
        if ls == lt == 0:
            return False
        
        if lt - ls > 1:
            return False
        elif lt - ls == 1:
            # delete or insert
            for i in range(ls):
                if s[i] != t[i]:
                    return s == t[:i] + t[i+1:]
            return True
        else:
            # replace
            for i in range(ls):
                if s[i] != t[i]:
                    return s[i+1:] == t[i+1:]
            return False


# One pass
# Time: O(N), N is the length of s
# Space: O(1)
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        if ls > lt:
            # 1st str has shorter length
            return self.isOneEditDistance(t, s)
        
        if lt - ls > 1:
            return False
        
        for i in range(ls):
            if s[i] != t[i]:
                if ls == lt:
                    return s[i+1:] == t[i+1:]
                else:   # ls == lt - 1
                    return s[i:] == t[i+1:]
        
        # if there is no diffs on ls distance
        # the strings are one edit away only if t has one more char
        return ls == lt - 1
