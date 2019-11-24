"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701


Solution:
26-coded Convention
"""


# Time: O(n), n is the length of s
# Space: O(1)
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        l = len(s)
        for i in range(l):
            power = l - i - 1
            res += 26 ** power * (ord(s[i]) - ord('A') + 1)
        return res
        
