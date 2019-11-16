"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49


Solution:
1. Brute Force
Consider each pair

2. Two Pointers
Every time we move the shorter-line pointer forward, cause that may increase the area. 移动短边才可能让面积更大
"""


# Two Pointers
# Time: O(n)
# Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        i, j = 0, l - 1
        res = 0
        left_bar, right_bar = 0, 0
        
        # most_water = min(height[i], height[j]) * x_axis_length
        while i < j:
            water = (j - i) * min(height[i], height[j])
            if water > res:
                res = water
                left_bar, right_bar = i, j
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return res
