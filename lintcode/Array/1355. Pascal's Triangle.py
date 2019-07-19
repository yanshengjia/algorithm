"""
Description:
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Solution:
逐行递推，注意 corner case
"""


class Solution:
    """
    @param numRows: num of rows
    @return: generate Pascal's triangle
    """
    def generate(self, numRows):
        # write your code here
        res = []
        if numRows == 0:
            return res
        for i in range(numRows):
            if i == 0:
                res.append([1])
            else:
                row_len = i + 1
                row = [0 for i in range(row_len)]
                row[0], row[-1] = 1, 1
                for j in range(1, row_len-1):
                    row[j] = res[i-1][j-1] + res[i-1][j]
                res.append(row)
        return res
            