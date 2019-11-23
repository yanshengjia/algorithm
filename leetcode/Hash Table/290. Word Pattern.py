"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.


Solution:
Use 2 hashmap to keep track of the mappings between words and patterns.
word2pattern
pattern2word
"""


# Hashtable
# Time: O(n), n is the length of pattern
# Space: O(n)
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        d = dict()
        dd = dict()
        words = str.split(' ')
        if len(pattern) != len(words):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = words[i]
            else:
                if d[pattern[i]] != words[i]:
                    return False
            
            if words[i] not in dd:
                dd[words[i]] = pattern[i]
            else:
                if dd[words[i]] != pattern[i]:
                    return False
            
        return True
        