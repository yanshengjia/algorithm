"""
Description:
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed. For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Solution:
模拟题，按照题意写就行
"""


class Solution:
    """
    @param A: a matrix
    @return: the resulting image
    """
    def flipAndInvertImage(self, A):
        # Write your code here
        for i in range(len(A)):
            A[i].reverse()
            for j in range(len(A[i])):
                A[i][j] = 1 - A[i][j]
        return A
