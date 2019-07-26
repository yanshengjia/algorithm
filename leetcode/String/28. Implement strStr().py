"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


Solution:
if string needle is empty, return 0
if string haystack is empty, return -1
for loop is faster than while loop

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_h, len_n = len(haystack), len(needle)
        if len_n == 0:
            return 0
        i = 0
        for i in range(len_h - len_n + 1):
            if haystack[i:i+len_n] == needle:
                return i
        return -1
