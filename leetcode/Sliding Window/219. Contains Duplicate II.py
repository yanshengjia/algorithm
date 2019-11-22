"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Solution:
Sliding winodw
Maintain a k-size window
"""


# Sliding Window
# Time: O(N), N is the length of nums
# Space: O(k)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i in range(len(nums)):
            if nums[i] in window and len(window) <= k+1:
                return True
            
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i-k])
        return False