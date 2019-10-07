"""
Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

Example 1:

Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest arithmetic subsequence is [1,2,3,4].
Example 2:

Input: arr = [1,3,5,7], difference = 1
Output: 1
Explanation: The longest arithmetic subsequence is any single element.
Example 3:

Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is [7,5,3,1].


Solution:
Hashtable
We can use a hashmap to record the length of LAS which ends at A as dict[A]
If the key 'A - difference' in the dict, it means there is a element in the previous array which can form a LAS with cur element.
So we increment the length, d[A] = d[A-difference] + 1. In the mean while, update the max length.
"""


# Time: O(N), N is the length of arr
# Space: O(M), M is the number of unique numbers in arr
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = 1
        d = dict()  # d[a] represent the length of las end at a
        for a in arr:
            if a - difference not in d: # no sequence, a is the start
                d[a] = 1
            else:   # a in a sequence
                d[a] = d[a - difference] + 1
                res = max(res, d[a])    
        return res
        