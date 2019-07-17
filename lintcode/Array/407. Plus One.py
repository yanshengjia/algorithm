"""
Description:
Given a non-negative number represented as an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.

Solution:
将数组中的数字组合，加一，再拆分
"""


class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        # write your code here
        s = ""
        for i in digits:
            s += str(i)
        num = int(s)
        res_num = num + 1
        res = []
        while res_num > 0:
            res.append(res_num % 10)
            res_num //= 10
        res.reverse()
        return res
