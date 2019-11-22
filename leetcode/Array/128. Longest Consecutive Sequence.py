"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


Solution:
1. Sort
2. Hashset
"""


# Sort
# TLE: while loop too slow
# Time: O(NlogN)
# Space: O(1)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        
        nums.sort()
        
        max_len = 0
        for i in range(l):
            cur_len = 1
            j = i + 1
            while j < l:
                if nums[j] == nums[j-1] + 1:
                    cur_len += 1
                    j += 1
                elif nums[j] == nums[j-1]:
                    j += 1
                else:
                    break
            if cur_len > max_len:
                max_len = cur_len
            i = j
        return max_len


# Sort
# Time: O(NlogN)
# Space: O(1)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        
        nums.sort()
        
        max_len = 0
        cur_len = 1
        for i in range(1, l):
            if nums[i] != nums[i-1]:
                # jump duplicates
                if nums[i] == nums[i-1] + 1:
                    cur_len += 1
                else:
                    max_len = max(max_len, cur_len)
                    cur_len = 1
        
        # in case of the last number is in the longest consecutive numbers
        max_len = max(max_len, cur_len)
        return max_len


# Sort
# Time: O(NlogN)
# Space: O(1)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l < 2 :
            return l

        res = 0
        cur_len = 1

        nums = list(set(nums))
        nums.sort()

        for i in range(1, len(nums)) :
            if nums[i] == nums[i-1]+1 :
                cur_len += 1
            else:
                res = max(res, cur_len)
                cur_len = 1

        res = max(res, cur_len)
        return res


# Set
# Time: O(N), since we visit each number once
# Space: O(1)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for each num I will check whether num-1 exists
        # if yes, then I ignore this num
        # Otherwise if num-1 doesn't exist, then I will go till I can find num+1
        # so in a way I am only checking each number max once and once in set.
    
        s = set(nums)
        
        res = 0
        
        for num in s:
            cur_len = 1
            if num - 1 not in s:
                while num + 1 in s:
                    cur_len += 1
                    num += 1
                res = max(res, cur_len)
        
        return res