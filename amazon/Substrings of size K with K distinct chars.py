"""
Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

Example 1:

Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]
Example 2:

Input: s = "abacab", k = 3
Output: ["bac", "cab"]
Example 3:

Input: s = "awaglknagawunagwkwagl", k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
Explanation: 
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl" 
"wagl" is repeated twice, but is included in the output once.
"""


def unique_substring(s: str, k: int) -> list:
    if not s or k == 0:
        return []
    l = len(s)
    res = []
    for i in range(l - k + 1):
        window = s[i:i+k]
        if len(set(window)) == k and window not in res:
            res.append(window)
    return res


def unique_substring_2(s: str, k: int) -> list:
    if not s or k == 0:
        return []
    
    l = len(s)
    char = dict()
    res = []
    i, j = 0, 0
    while i <= j and j < l:
        char[s[j]] = char.get(s[j], 0) + 1
        while char[s[j]] > 1:  # cur window not valid, push i forward
            char[s[i]] -= 1
            i += 1

        if j - i + 1 == k:
            sub_s = s[i:j+1]
            if sub_s not in res:
                res.append(sub_s)
            
            # i quit
            char[s[i]] -= 1
            i += 1

        j += 1
    return res


if __name__ == "__main__":
    # s = "abcabc"
    # k = 3
    # s = "abacab"
    # k = 3
    s = "awaglknagawunagwkwagl"
    k = 4
    print(unique_substring_2(s, k))
