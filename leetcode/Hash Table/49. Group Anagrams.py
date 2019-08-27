"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.


Solution:
1. Categorize by Sorted String
Maintain a map ans : {String -> List} where each key \text{K}K is a sorted string, and each value is the list of strings from the initial input that when sorted, are equal to \text{K}K.

In Java, we will store the key as a string, eg. code. In Python, we will store the key as a hashable tuple, eg. ('c', 'o', 'd', 'e').

2. Categorize by Count (Hash Table)
"""


# Categorize by Sorted String
# Time Complexity: O(NKlogK), where N is the length of strs, and K is the maximum length of a string in strs. The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.
# Space: O(NK), the total information content stored in ans. 
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()


# Categorize by Count
# Hash table
# Use a 26-length tuple to record the frequency of chars in a word based on ascii code.
# Time Complexity: O(NK), where N is the length of strs, and K is the maximum length of a string in strs. Counting each string is linear in the size of the string, and we count every string.
# Space: O(NK), the total information content stored in ans. 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()  # {anagram_hashtable: [word1, word2, word3]}
        res = []
        for word in strs:
            h_str = self.hash(word)
            if h_str not in d:
                d[h_str] = [word]
            else:
                d[h_str].append(word)
        
        for k, v in d.items():
            res.append(v)
        return res
    
    
    def hash(self, word):
        h = [0] * 26
        for char in word:
            h[ord(char) - ord('a')] += 1
        return tuple(h)


# Categorize by Count
class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()