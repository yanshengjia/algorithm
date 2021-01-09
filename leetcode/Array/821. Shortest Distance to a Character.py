"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:
* S string length is in [1, 10000].
* C is a single character, and guaranteed to be in string S.
* All letters in S and C are lowercase.


Soultion:
1. Min Array. The min distance is either the distance from the left `C` or the distance from the right `C`.
For each index S[i], let's try to find the distance to the next character C going left, and going right. The answer is the minimum of these two values.

2. Memorize locations of char C
Two pass.
"""


# Memorize locations of C and two pass scan
# TC: O(N), N = len(S)
# SC: O(N+M), M = number of C
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        locations = []
        for i in range(len(S)):
            if S[i] == C:
                locations.append(i)
        
        res = []
        idx = 0
        for i in range(len(S)):
            loc = locations[idx]
            if i < loc:
                distance = loc - i
            elif i == loc:
                distance = 0
            else:
                if loc == locations[-1]:
                    distance = i - loc
                else:
                    left_dist = i - locations[idx]
                    right_dist = locations[idx+1] -i
                    distance = min(left_dist, right_dist)
                    if right_dist <= left_dist:
                        idx += 1
            res.append(distance)
        return res


# Min Array
# Left -> Right pass and Right -> left pass
# TC: O(N)
# SC: O(N)
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        pre = float('-inf')
        res = []
        
        # left -> right
        for i in range(len(S)):
            if S[i] == C:
                pre = i
            res.append(i - pre)
        
        # right -> left
        pre = float('inf')
        for i in range(len(S)-1, -1, -1):
            if S[i] == C:
                pre = i
            res[i] = min(res[i], pre-i)
        return res
