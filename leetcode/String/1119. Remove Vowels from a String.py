"""
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

Example 1:
Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"


Solution:
1. scan the string S, jump all vowels
2. re  re.sub('a|e|i|o|u', '', S)
3. replace
"""


# time-O(n)
# space-O(n)
class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        res = ''
        for c in S:
            if c not in vowels:
                res += c
        return res
        