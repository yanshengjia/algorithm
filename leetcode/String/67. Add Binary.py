"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Solution:
1. Bit Manipulation
2. Iterative
"""


# Iterative
# Time: O(max(len_a, len_b))
# Space: O(len_a + len_b)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la, lb = list(a)[::-1], list(b)[::-1]
        i, j, carry = 0, 0, 0
        res = []
        while i < len(la) and j < len(lb):
            s = int(la[i]) + int(lb[j]) + carry
            if s > 1:
                carry = 1
            else:
                carry = 0
            res.append(s % 2)
            i += 1
            j += 1
        
        # a is longer
        while i < len(la):
            s = int(la[i]) + carry
            if s > 1:
                carry = 1
            else:
                carry = 0
            res.append(s % 2)
            i += 1
        
        # b is longer
        while j < len(lb):
            s = int(lb[j]) + carry
            if s > 1:
                carry = 1
            else:
                carry = 0
            res.append(s % 2)
            j += 1
        
        if carry == 1:
            res.append(1)
        
        return ''.join([str(e) for e in res[::-1]])


# Iterative
# No need to reverse, iterate backwards and build the result from the back by adding two last digits while keeping carry in mind.
# In the end, if carry is non-zero we append it to the front.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            a_digit = int(a[i]) if i >= 0 else 0
            b_digit = int(b[j]) if j >= 0 else 0
            _sum = a_digit + b_digit + carry    # temp sum for 2 difits from a and b
            digit = _sum % 2
            carry = _sum // 2
            result = str(digit) + result
            i -= 1
            j -= 1
        if carry:
            result = str(carry) + result
        return result


# Bit Operation
# Time: O(max(len_a, len_b))
# Space: O(max(len_a, len_b))
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a,2)     # convert a into binary
        y = int(b,2)     # convert b into binary
        z = bin(x+y)      # adds both integer converted values  and converts in into binary
        return z[2::]   # python binary prints 100 binary value like 0b100 slicing first 2 values returns the output
        
