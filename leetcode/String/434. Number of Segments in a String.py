"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5

Solution:
1. Count the segment in place
2. Built-in function split()
"""

# Built-in
# Time: O(N)
# Space: O(N)
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


# In place
# Time: O(N)
# Space: O(1)
class Solution:
    def countSegments(self, s):
        segment_count = 0

        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                segment_count += 1

        return segment_count