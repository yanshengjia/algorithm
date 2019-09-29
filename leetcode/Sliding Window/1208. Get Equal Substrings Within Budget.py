"""
You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.

You are also given an integer maxCost.

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of twith a cost less than or equal to maxCost.

If there is no substring from s that can be changed to its corresponding substring from t, return 0.


Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.
Example 2:

Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to charactor in t, so the maximum length is 1.
Example 3:

Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You can't make any change, so the maximum length is 1.


Solution:
Calculate the differences between a[i] and b[i]
Use a sliding window to track the longest valid substring.
"""


# Sliding window
# Time: 
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        len_s = len(s)
        diff = [0] * len_s
        for i in range(len_s):
            diff[i] = abs(ord(s[i]) - ord(t[i]))
        # print(diff)
        
        # sliding window
        start = 0
        end = 0
        res = 0
        sum = diff[0]

        while (start < len_s and end < len_s) : 
            # If sum is less than k, 
            # move end by one position. 
            # Update count and sum 
            # accordingly. 
            if sum <= maxCost: 
                end += 1

                if end >= start:
                    if end - start > res:
                        res = end - start 

                # For last element, end may become n 
                if end < len_s: 
                    sum += diff[end] 

            # If sum is greater than or equal to k,  
            # subtract arr[start] from sum and 
            # decrease sliding window by moving  
            # start by one position 
            else :  # sum > maxCost
                sum -= diff[start]
                start += 1
        return res
