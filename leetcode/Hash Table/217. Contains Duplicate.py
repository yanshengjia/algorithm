"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true


Solution:
1. Hash Table
2. Sorting. If there are any duplicate integers, they will be consecutive after sorting.
"""


# Time-O(N), We do search() and insert() for n times and each operation takes constant time.
# Space-O(N), The space used by a hash table is linear with the number of elements in it.
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = dict()
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                return True
        return False
        