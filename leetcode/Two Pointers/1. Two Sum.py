# https://leetcode.com/problems/two-sum/description/


# Solution 1: Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# Solution 2: Two Pass Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}

        for i in range(len(nums)):
            d[nums[i]] = i  # {nums_value: index}
        
        for j in range(len(nums)):
            complement = target - nums[j]
            if complement in d and d[complement] != j: # can't use same element twice
                return [j, d[complement]]

        return []

# Solution 3: One Pass Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d: # insert elements into hash table and look back
                return [i, d[complement]]
            d[nums[i]] = i
        return []
        