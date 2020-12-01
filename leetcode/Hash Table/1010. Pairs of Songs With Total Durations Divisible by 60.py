"""
In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.


Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.


Solution:
TWO SUM VARIANT
Modulo distributive operation:
(a + b) mod n = [(a mod n) + (b mod n)] mod n

(a+b)%60=0
-> ((a%60) + (b%60))%60 = 0
-> a%60 = 0, b%60 = 0 or (a%60) + (b%60) = 60

if a%60 = 0, b%60 = 0
else, b%60 = 60 - a%60

-> b%60 = (60 - a%60) %60 = -a%60


Use an array remainders with size 60 to record the frequencies of each remainder - as the range of remainders is [0, 59]
"""


# b%60 = (60 - a%60) %60 = -a%60
# Time: O(N), N = len(time)
# Space: O(1)
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = [0] * 60   # record t%60
        res = 0
        for t in time:
            res += remainders[-t%60]
            remainders[t%60] += 1
        return res


# if a%60 = 0, b%60 = 0
# else a%60 != 0, b%60 = 60 - a%60
# Time: O(N), N = len(time)
# Space: O(1)
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = [0] * 60   # record t%60
        res = 0
        for t in time:
            if t % 60 == 0:
                res += remainders[0]
            else:
                res += remainders[60 - t%60]
            remainders[t % 60] += 1
        return res
