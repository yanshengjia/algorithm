"""
Description:
Count the number of k's between 0 and n. k can be 0 - 9.

Solution:
O(n^2) 遍历每个数字，count 每个数字中 k 的个数
"""


class Solution:
    """
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
    # write your code here
        c = 0
        k_char = str(k)
        for i in range(n+1):
            num = str(i)
            c += num.count(k_char)
        return c