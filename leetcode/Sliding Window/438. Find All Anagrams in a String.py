"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Solution:
Sliding Window
"""


# Time: O(n), n is the length of s
# Space: O(1)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        table_p = [0] * 26
        table_s = [0] * 26
        
        for c in p:
            table_p[ord(c)-ord('a')] += 1
        
        str_p = "".join([str(c) for c in table_p])
        
        res = []
        l_s, l_p = len(s), len(p)
        for i in range(l_s):
            table_s[ord(s[i])-ord('a')] += 1
            if i < l_p - 1:
                continue
            else:
                start = i + 1 - l_p
                
                if table_p == table_s:
                    res.append(start)
                table_s[ord(s[start])-ord('a')] -= 1
        
        return res
    