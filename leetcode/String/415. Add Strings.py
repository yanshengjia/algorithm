"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))


# Time: O(m+n)
# Space: O(1)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carrier, res = len(num1)-1, len(num2)-1, 0, ""
        while i >= 0 or j >=0 or carrier:
            if i >= 0:
                carrier += (ord(num1[i]) - ord('0'))
                i -= 1
            if j >= 0:
                carrier += (ord(num2[j]) - ord('0'))
                j -= 1
            res += str(carrier % 10)
            carrier //= 10
        return res[::-1]
