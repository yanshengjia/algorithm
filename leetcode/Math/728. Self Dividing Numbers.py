"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]


Solution:
Brute Force
For each number in the given range, we will directly test if that number is self-dividing.

For each number in the range, check whether it is self dividing by converting that number to a character array (or string in Python), then checking that each digit is nonzero and divides the original number.
"""


# Time Complexity: O(D), where D is the number of integers in the range [L, R], and assuming log(R) is bounded. (In general, the complexity would be O(DlogR).)
# Space Complexity: O(D), the length of the answer.
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            if self.isSelfDividingNumber(i):
                res.append(i)
        return res
    
    def isSelfDividingNumber(self, num):
        digits = []
        t = num
        while t > 0:
            r = t % 10
            if r == 0:
                return False
            digits.append(r)
            t //= 10
        for d in digits:
            if num % d != 0:
                return False
        return True
        
