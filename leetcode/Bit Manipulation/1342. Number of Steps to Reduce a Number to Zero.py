'''
Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.


Example 1:

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
Example 2:

Input: num = 8
Output: 4
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.
Example 3:

Input: num = 123
Output: 12

Constraints:
0 <= num <= 10^6


Solution:
1. Simulation
2. Bit Manipulation
For the binary representation from right to left(until we find the leftmost 1):
if we meet 0, result += 1 because we are doing divide;
if we meet 1, result += 2 because we first do "-1" then do a divide;
ony exception is the leftmost 1, we just do a "-1" and it becomse 0 already.
'''


# Simulation
# Time: O(logN), N is num
# Space: O(1)
class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            steps += 1
        return steps


# Bit Manipulation
# Time: O(1)
# Space: O(1)
class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            return 0
        
        res = 0
        while num != 0:
            if num & 1:    # even
                res += 2
            else:   # odd
                res += 1
            # res += (num & 1) + 1    
            num >>= 1   # rightshift 1 bit
        return res - 1
        

