"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6


Solution: https://leetcode.com/problems/trapping-rain-water/solution/
For each element in array, the water it can trap depends on min of max heights of both sides of this element.

1. DP
Get accumulative max heights for both sides, max_left and max_right
max_trap_water = min(max_left[i], max_right[i]) - height[i]

2. Stack
use stack to keep track of the bars that are bounded by longer bars and hence, may store water. Using the stack, we can do the calculations in only one iteration.
We keep a stack and iterate over the array. We add the index of the bar to the stack if bar is smaller than or equal to the bar at top of stack, which means that the current bar is bounded by the previous bar in the stack. If we found a bar longer than that at the top, we are sure that the bar at the top of the stack is bounded by the current bar and a previous bar in the stack, hence, we can pop it and add resulting trapped water to ans.

3. Two Pointers (Optimal)
If there is a larger bar at one end (say right), we are assured that the water trapped would be dependant on height of bar in current direction (from left to right).
As soon as we find the bar at other end (right) is smaller, we start iterating in opposite direction (from right to left). We must maintain left_max and right_max during the iteration, but now we can do it in one iteration using 2 pointers, switching between the two.
Time: O(n) Space: O(1)
"""


# DP
# Time: O(n)
# Space: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        if l == 0:
            return 0
        
        max_left = [0 for _ in range(l)]
        max_right = [0 for _ in range(l)]
        
        # get accumulative max left side height
        cur_max = 0
        for i in range(l):
            if height[i] > cur_max:
                cur_max = height[i]
            max_left[i] = cur_max
        
        # get accumulative max right side height
        cur_max = 0
        for i in range(l-1, -1, -1):
            if height[i] > cur_max:
                cur_max = height[i]
            max_right[i] = cur_max
        
        # max_trap_water = min(max_left[i], max_right[i]) - height[i]
        res = 0
        for i in range(l):
            res += min(max_left[i], max_right[i]) - height[i]
        return res


# Two Pointets
# Time: O(n)
# Space: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        if l == 0:
            return 0
        
        left_max, right_max = 0, 0
        i, j = 0, l - 1
        
        res = 0
        while i < j:
            if height[i] < height[j]:
                # the water trapped depends on height of bar in left->right direction
                if height[i] > left_max:
                    left_max = height[i]
                else:
                    res += left_max - height[i]
                i += 1
            else:
                # the water trapped depends on height of bar in right->left direction
                if height[j] > right_max:
                    right_max = height[j]
                else:
                    res += right_max - height[j]
                j -= 1
        
        return res
