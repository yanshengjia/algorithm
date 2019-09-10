"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
Example 1:

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.


Solution:
1. First find all valid starting points and then travel around. Time: O(N^2)
2. One Pass, using total_tank and cur_tank to store the states of the tank
* For a valid starting point, gas[i] >= cost[i]
* To station i, if cur_tank < 0, cant travel around for the starting point. So we have to update starting point as i+1
* If total_tank < 0, fail. total_tank means the sum of (gas[i] - cost[i])
"""


# Brute Force
# Time: O(N^2), TLE
# Space: O(N), where N is the number of gas station
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = []
        n = len(gas)
        left = [0] * n
        for i in range(n):
            left[i] = gas[i] - cost[i]
            if left[i] >= 0:
                start.append(i)
        
        if len(start) == 0:
            return -1
        
        j = 0
        while j < len(start):
            unvalid = False
            s = start[j]
            tank = left[s]
            for i in range(n):
                tank += left[(s+i+1)%n]
                if tank < 0:
                    start.remove(s)
                    unvalid = True
                    break
            if not unvalid:
                j += 1
        if len(start) == 0:
            return -1
        else:
            return start[0]
    


# One pass
# Time: O(N), > 99%, where N is the number of gas station
# Space: O(1)
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        total_tank, cur_tank = 0, 0
        start = 0
        
        for i in range(n):
            total_tank += gas[i] - cost[i]
            cur_tank += gas[i] - cost[i]
            
            # if car cant reach station i
            if cur_tank < 0:
                # update starting station
                start = i + 1
                # reset cur_tank gas
                cur_tank = 0
        
        return start if total_tank >= 0 else -1
