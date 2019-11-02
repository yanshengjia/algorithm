"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]

Follow up:
It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.


Solution:
x &= (x-1) bitwise AND 与，remove the least significant 1 of x
"""


# Time: O(n*sizeof(int))
# Space: O(n)
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num+1):
            res.append(self.count_one(i))
        return res
    
    def count_one(self, n):
        count = 0
        while n != 0:
            n &= (n-1)
            count += 1
        return count