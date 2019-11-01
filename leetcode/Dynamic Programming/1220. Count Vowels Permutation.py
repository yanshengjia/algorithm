"""
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.


Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3: 

Input: n = 5
Output: 68


Solution:
1. BFS
2. DP
dp[len][vowel]: a list of dict, key is vowel, value is int number. The quantity of possible strings of length+1 ends with vowel

dp[i][v] init to 0, we can use collections.defaultdict(int) so that the default value of a key in dict is 0
dp[i][rules[v]] += dp[i-1][v]
"""


# Time: O(n)
# Space: O(n)
import collections
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [collections.defaultdict(int) for i in range(n)]
        vowels = ['a', 'e', 'i', 'o', 'u']
        rules = {
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }
        
        for v in vowels:
            dp[0][v] = 1
        
        for i in range(1, n):
            for k, v in rules.items():
                for c in v:
                    dp[i][c] += dp[i-1][k]
        
        res = sum(dp[-1].values()) % mod
        return res


