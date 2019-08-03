"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2


Solution:
1. linear search
2. binary search
"""


# linear search
# Time-O(N), where N is the length of nums
# Space-O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                index = i
                break
        return index



# binary search
# Time-O(logN), where N is the length of nums
# Space-O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target <= nums[0]:
            return 0
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            mid = (i+j) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid
                if i == j - 1:
                    return j
            else:
                j = mid
        