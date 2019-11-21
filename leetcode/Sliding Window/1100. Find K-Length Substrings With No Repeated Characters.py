"""
Given a string S, return the number of substrings of length K with no repeated characters.


Example 1:

Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation: 
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: S = "home", K = 5
Output: 0
Explanation: 
Notice K can be larger than the length of S. In this case is not possible to find any substring.


Solution:
1. Sliding window with checking each K-length window + Dict
2. Sliding window with 2 pointers + Set
"""


# Sliding window with checking each K-length window + Dict
# Time: O(N), N is the length of S
# Space: O(1)
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        l = len(S)
        if l < K:
            return 0
        
        res = 0
        d = dict()
        for i in range(K):
            d[S[i]] = d.get(S[i], 0) + 1
        
        if self.is_repeated(d):
            res += 1
        
        for i in range(1, l-K+1):
            # remove S[i-1]
            d[S[i-1]] -= 1
            if d[S[i-1]] == 0:
                del d[S[i-1]]
            d[S[i+K-1]] = d.get(S[i+K-1], 0) + 1
            if self.is_repeated(d):
                res += 1
        return res
        
    
    def is_repeated(self, d):
        for k, v in d.items():
            if v != 1:
                return False
        return True
        

# Sliding window + set
# Time: O(N)
# Space: O(1)
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        l = len(S)
        if l < K:
            return 0
        
        res = 0
        window = set()
        i, j = 0, 0
        
        for j in range(l):
            # cur i is not a potential valid start, increment it
            while S[j] in window:
                window.remove(S[i])
                i += 1
            
            # add new char
            window.add(S[j])
            
            if j - i + 1 == K:
                # K-length no repeated chars
                res += 1
                window.remove(S[i])
                i += 1
        return res
        