"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false


Solution:
1. Recursion + Backtracking
2. Recursion + Memo
3. BFS
4. DP
"""


# Recursion + Backtracking
# Time: O(n^n), Consider the worst case where ss = "\text{aaaaaaa}aaaaaaa" and every prefix of ss is present in the dictionary of words, then the recursion tree can grow upto n^n
# Space: O(n), the depth of recursion tree can go up to 2
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.recursive(s, wordDict, 0)
    
    
    def recursive(self, s: str, wordDict: List[str], start: int):
        if start == len(s):
            return True
        
        for end in range(start+1, len(s)+1):
            if s[start:end] in wordDict and self.recursive(s, wordDict, end):
                return True
        return False


# DP
# Time: O(n)
# Space: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        dp = [False for _ in range(l+1)] # dp[i] == True represents s[:i] can be a valid word break
        dp[0]= True
        
        for i in range(l):
            if dp[i]:
                for word in wordDict:
                    j = len(word)
                    if i + j <= l and s[i:i+j] == word:
                        dp[i+j] = True
        return dp[-1]

