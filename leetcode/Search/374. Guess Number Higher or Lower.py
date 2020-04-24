"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6


Solution:
Binary Search
Here "My" means the number which is given for you to guess not the number you put into guess(int num).
Bad description.
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


# Binary Search
# Time: O(logn)
# Space: O(1)
class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        low, high = 1, n
        while low <= high:
            mid = int((low + high) / 2)
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                low = mid + 1
            else:
                high = mid - 1
