"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.


Solution:
Binary Search
compare mid^2 (mid+1)^2 with x
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 0, x
        while left < right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                if (mid+1) * (mid+1) < x:
                    left = mid
                elif (mid+1) * (mid+1) == x:
                    return mid+1
                else:
                    return mid
            else:
                right = mid
        return mid
