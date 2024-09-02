"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:
* 1 <= s.length <= 1000
* s consists of English letters (lower-case and upper-case), ',' and '.'.
* 1 <= numRows <= 1000


Solution:
This problem is a string simulation. Logic is easy, just many edge cases to handle, for example numRows == 1 or 2.
"""

# Time: O(n), n is the length of str
# Space: O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:  # edge case
            return s

        if numRows == 2:  # edge case
            numCols = ceil(len(s) / 2)
        elif len(s) % (numRows + 1) == 0:
            numCols = (numRows - 1) * (len(s) // (numRows + 1))
        else:
            numCols = (numRows - 1) * (len(s) // (numRows + 1)) + 1

        s_2d = [[0 for j in range(numCols)] for i in range(numRows)]

        c = 0
        # scan the string
        i = 0
        while i < len(s):
            # record the vertical line
            for j in range(0, numRows):
                if i >= len(s): break
                s_2d[j][c] = s[i]
                i += 1
            
            c += 1  # move to next column

            # record the diagonal line
            for k in range(0, numRows - 2):
                if i >= len(s): break
                s_2d[numRows - 2 - k][c] = s[i]
                i += 1
                c += 1  # move to next column
    
        res = ""
        for i in range(0, numRows):
            for j in range(0, numCols):
                if s_2d[i][j] != 0:
                    res += s_2d[i][j]
        return res
