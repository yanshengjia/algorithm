"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:

Input:
"bbbab"

Output:
4
One possible longest palindromic subsequence is "bbbb".

Example 2:
Input:
"cbbd"

Output:
2
One possible longest palindromic subsequence is "bb".


Solution:
1. Recursion
2. Recursion + Memo
3. 2D DP
dp[i][j]: the length of LPS in s[i:j+1]

dp[i][j] = 1, if i == j
		 = dp[i+1][j-1] + 2, if  s[i] == s[j] and i < j - 1
	     = max(dp[i-1][j], dp[i][j-1]) , if  s[i] != s[j] and i < j - 1
"""


# Recursion
# TLE
# Time: O(2^n)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.lps(0, len(s)-1, s)
    
    def lps(self, l, r, s):
        if l == r:
            return 1
        elif l > r:
            return 0
        else:
            if s[l] == s[r]:
                return 2 + self.lps(l+1, r-1, s)
            else:
                return max(self.lps(l+1, r, s), self.lps(l, r-1, s))
        

# Recursion + Memo
# store the intermediate result in the process of DFS, each lps[i][j] only computed once
# Time: O(n^2)
# Space: O(n^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        self.memo = [[0 for _ in range(len(s))] for _ in range(len(s))]
        return self.lps(0, len(s)-1, s)
    
    def lps(self, l, r, s):
        if l == r:
            return 1
        if l > r:
            return 0
        if self.memo[l][r] != 0:
            return self.memo[l][r]
        else:
            if s[l] == s[r]:
                self.memo[l][r] = 2 + self.lps(l+1, r-1, s)
            else:
                self.memo[l][r] = max(self.lps(l+1, r, s), self.lps(l, r-1, s))
            return self.memo[l][r]


# 2D DP
# Time: O(n^2)
# Space: O(n^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        l = len(s)
        dp = [[1 for _ in range(l)] for _ in range(l)]
        
        # len = 2
        for i in range(l-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 2
        
        # len starts at 3
        for ll in range(2, l):
            for i in range(l-ll):
                j = i + ll
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    # 2 chars at both sides cannot contibute to lps at the same time
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][l-1]


# 1D DP
# In #3, the current row is computed from the previous 2 rows only. So we don't need to keep all the rows.
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        l = len(s)
        
        # 1D DP, cur row only depends on the previous 2 rows.
        first, second, third = [1 for _ in range(l)], [1 for _ in range(l)], [1 for _ in range(l)]
        
        # len = 2
        for i in range(l-1):
            if s[i] == s[i+1]:
                second[i] = 2
        
        # len starts at 3
        for ll in range(2, l):
            for i in range(l-ll):
                
                j = i + ll
                if s[i] == s[j]:
                    third[i] = first[i+1] + 2
                else:
                    # 2 chars at both sides cannot contibute to lps at the same time
                    third[i] = max(second[i], second[i+1])
            
            # update previous 2 rows, deepcopy
            first = second[:]
            second = third[:]
        
        if l == 0:
            return 0
        elif l == 1:
            return first[0]
        elif l == 2:
            return second[0]
        else:
            return third[0]
