"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Solution:
1. Expand around center
2. DP
"""


# Expand around center
# Time: O(n^2)
# Space: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        l = len(s)
        
        for i in range(2*l - 1):
            # center index = i, even indexes exist, odd indexes don't exist
            if i % 2 == 0:
                res += 1
                for ll in range(2, l, 2):
                    left = (i - ll) // 2
                    right = (i + ll) // 2
                    if left >= 0 and right < l:
                        if s[left] == s[right]:
                            res += 1
                        else:
                            break
            else:
                for ll in range(1, l, 2):
                    left = (i - ll) // 2
                    right = (i + ll) // 2
                    if left >= 0 and right < l:
                        if s[left] == s[right]:
                            print(left, right)
                            res += 1
                        else:
                            break
        return res



# DP
# Time: O(n^2), n is the length of s
# Space: O(n^2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        l = len(s)
        
        # dp[i][j]: is substring s[i:j+1] is a palindrome
        dp = [[0 for _ in range(l)] for _ in range(l)]
        
        # i: left pointer, j: right pointer
        for j in range(l):
            for i in range(j+1):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = 1
                    elif i+1 < l and j-1 >= 0 and dp[i+1][j-1] == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                else:
                    dp[i][j] = 0
                
                if dp[i][j] == 1:
                    cnt += 1
        return cnt
