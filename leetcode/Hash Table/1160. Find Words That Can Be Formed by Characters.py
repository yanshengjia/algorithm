"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.


Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


Solution:
Use hashmap to record the frequency of each char in chars.
Check whether the char in word is in the hashmap and make sure the frequency of char in word is smaller than it in hashmap.
"""


# Hashmap
# Time: O(Nk), > 5%, where N is the length of words, k is the average length of word in words
# Space: O(1)
import copy
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = dict()
        for c in chars:
            d[c] = d.get(c, 0) + 1
        
        res = 0
        for word in words:
            if self.isGoodString(word, d):
                res += len(word)
        return res
    
    def isGoodString(self, s: str, d: dict) -> bool:
        dd = copy.deepcopy(d)
        for c in s:
            if c not in dd:
                return False
            else:
                dd[c] -= 1
                if dd[c] < 0:
                    return False
        return True


# List
# Time: > 60%
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for w in words:
            good = True
            chars_l = [c for c in chars]
            for c in w:
                if c in chars_l:
                    chars_l.remove(c)
                else:
                    good = False
                    break
            if good:
                res += len(w)
        return res