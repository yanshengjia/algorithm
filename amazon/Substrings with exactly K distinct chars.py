"""
Given a string s and an int k, return an int representing the number of substrings (not unique) of s with exactly k distinct characters. If the given string doesn't have k distinct characters, return 0.
https://leetcode.com/problems/subarrays-with-k-different-integers

Example 1:

Input: s = "pqpqs", k = 2
Output: 7
Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]
Example 2:

Input: s = "aabab", k = 3
Output: 0
"""


def substring_k_distinct_chars(s: str, k: int) -> int:
    if not s or k == 0:
        return 0
    
    l = len(s)
    i, j = 0, 0
    window = set()
    while i < j and j < l:
        


        j += 1
