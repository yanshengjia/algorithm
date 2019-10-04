"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


Solution:
1. Brute Force. O(N^3)
2. Sliding window + Set, requires at most 2n steps
3. Sliding window optimized, Use a hashmap to record last index of an element
Instead of using a set to tell if a character exists or not, we could define a mapping of the characters to its index. Then we can skip the characters immediately when we found a repeated character.
The reason is that if s[j] have a duplicate in the range [i, j) with index j′, 
we don't need to increase ii little by little. 
We can skip all the elements in the range [i, j'] and let ii to be j' + 1 directly.
"""


# Sliding Windows
# Time: O(2n), In the worst case, each character will be visited twice.
# Space: O(min(m, n)). Same as the previous approach. We need O(k) space for the sliding window, where k is the size of the Set. The size of the Set is upper bounded by the size of the string nn and the size of the charset/alphabet m.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = set()   # store all the unique values in the sliding window
        i, j = 0, 0
        n = len(s)
        res = 0
        while i < n and j < n:
            # extend the sliding window
            if s[j] not in d:
                d.add(s[j])
                j += 1
                res = max(res, j-i)
            else:
                d.remove(s[i])
                i += 1
        return res
                

# Sliding window optimized
# Time: O(n), index j will iterate n times
# Space: O(1), constant size array
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = [0] * 128  # for ASCII
        i, j, n = 0, 0, len(s)
        res = 0
        for j in range(n):
            # print(i, j)
            i = max(i, pos[ord(s[j])])  # find the last index of s[j] in sliding window [i, j]
            res = max(j-i+1, res)
            pos[ord(s[j])] = j+1
        return res
                
        