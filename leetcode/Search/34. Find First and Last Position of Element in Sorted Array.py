"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


Solution:
1. Scan. Linear time
2. Binary Search
"""


# Binary Search
# Time: O(logN), N is the length of nums
# Space: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:        
        # find the leftmost target
        start_pos = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[l] == target:
                start_pos = l
                break
            
            if l == r:
                if nums[mid] == target:
                    start_pos = mid
                break
            
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                start_pos = mid
                r = mid - 1
            else:
                r = mid - 1
        
        # find the rightmost target
        end_pos = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[r] == target:
                end_pos = r
                break
            
            if l == r:
                if nums[mid] == target:
                    end_pos = mid
                break
            
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                end_pos = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return start_pos, end_pos