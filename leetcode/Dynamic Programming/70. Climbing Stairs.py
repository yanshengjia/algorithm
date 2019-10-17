"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Solution:
1. Recursion (TLE)
We take all possible step combinations i.e. 1 and 2, at every step. At every step we are calling the function climbStairsclimbStairs for step 1 and 2, and return the sum of returned values of both functions.
从台阶i到台阶n的路数 climbStairs(i,n) = climbStairs(i + 1, n) + climbStairs(i + 2, n) 
where i defines the current step and n defines the destination step.

2. Recursion with Memo (Bottom up)
Memorize/Store climbStairs(i,n)

3. DP
One can reach i th step in one of the two ways:
* Taking a single step from (i-1) th step.
* Taking a step of 2 from (i-2) th step.

4. Fibonacci Number
"""


# Recursion
# Time: O(2^n), size of the recursion tree will be 2^n
# Space: O(n). The depth of the recursion tree can go up to n
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.recursion(0, n)
    
    def recursion(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        return self.recursion(i+1, n) + self.recursion(i+2, n)


# Recursion with Memo
# Time: O(N), size of recursion tree can go upto n
# Space: O(N)
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n+1)
        return self.recursion(0, n, memo)
    
    def recursion(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:     # reuse memo
            return memo[i]
        memo[i] = self.recursion(i+1, n, memo) + self.recursion(i+2, n, memo)
        return memo[i]


# DP
# Time: O(N)
# Space: O(N)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]