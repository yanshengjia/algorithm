"""
Given an integer n, return the first n-line Yang Hui triangle.

Example 1:

Input : n = 4
Output :  
[
 [1]
 [1,1]
 [1,2,1]
 [1,3,3,1]
]


Solution:
Construct pascal triangle line by line.
"""


class Solution:
    """
    @param n: a Integer
    @return: the first n-line Yang Hui's triangle
    """
    def calcYangHuisTriangle(self, n):
        # write your code here
        if n == 0:
            return []
        elif n == 1:
            return [[1]]
        else:
            res = [[1]]
            for i in range(1, n):
                line = [1 for j in range(i+1)]
                for k in range(1, i):
                    line[k] = res[i-1][k-1] + res[i-1][k]
                res.append(line)
            return res
