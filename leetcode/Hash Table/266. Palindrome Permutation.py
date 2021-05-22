"""
Given a string s, return true if a permutation of the string could form a palindrome.


Example 1:
Input: s = "code"
Output: false

Example 2:
Input: s = "aab"
Output: true

Example 3:
Input: s = "carerac"
Output: true
 

Constraints:
* 1 <= s.length <= 5000
* s consists of only lowercase English letters.


Solution:
Use Hashtable to count every character.
This problem has 2 cases, palindrome length is odd and palindrome length is even.
At most we can have 1 char which has odd count.
"""


# Hash Table
# TC: O(N), N = len(s)
# SC: O(1), table size <= 128, probably using array to store counts is better
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count_table = {}
        for c in s:
            count_table[c] = count_table.get(c, 0) + 1
        
        threshold = 1
        for count in count_table.values():
            if count % 2 == 1:
                threshold -= 1
                if threshold < 0:
                    return False
        return True
