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
    distinct, prefix = 0, 0
    res = 0
    window = dict()
    while j < l:
        if s[j] in window and window[s[j]] != 0:
            window[s[j]] += 1
        else:
            distinct += 1
            window[s[j]] = 1
        
        if distinct > k:
            window[s[i]] -= 1
            prefix = 0
            distinct -= 1
            i += 1
        
        while window[s[i]] > 1:
            window[s[i]] -= 1
            i += 1
            prefix += 1
        
        if distinct == k:
            res += 1 + prefix

        j += 1
    return res


if __name__ == "__main__":
    s = "pqpqs"
    k = 2
    print(substring_k_distinct_chars(s, k))
