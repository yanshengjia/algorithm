"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.


Solution:
Index as hash key
We don't care about duplicates or non-positive integers. O(2n) = O(n)
First process data, make all the non-positive number and number which index exceed len to 1
Second, make all encountered indexes negative. If ele in nums, make nums[ele] = -abs(nums[ele])
Return the index of the first positive element.
"""


# Swap elements until nums[i] <= 0
# Avoid nums[i] == nums[nums[i]], if so, it will have infinite loop
# Pay attention to number l is in nums or not
# Time: O(N), >95%, where N is the length of nums
# Space: O(1), constant space
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # corner case
        if 1 not in nums:
            return 1
        
        # corner case
        l = len(nums)
        if l == 1 and nums[0] == 1:
            return 2
        
        for i in range(l):
            if nums[i] <= 0 or nums[i] > l:
                nums[i] = 1
        
        for i in range(l):
            while nums[i] > 0:
                if nums[i] == l:
                    nums[0] = -1
                    break
                t = nums[nums[i]]
                if t == nums[i]:
                    nums[t] = - abs(nums[t])
                    break
                if t > 0:
                    nums[nums[i]] = - abs(nums[nums[i]])
                    nums[i] = t
                else:
                    break

        for i in range(1, l):
            if nums[i] > 0:
                return i
        if nums[0] > 0:    # there is no 'l' in nums
            return l
        return l + 1   # there is at least one 'l' in nums
        
        

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Base case.
        if 1 not in nums:
            return 1
        
        # nums = [1]
        if n == 1:
            return 2
        
        # Replace negative numbers, zeros,
        # and numbers larger than n by 1s.
        # After this convertion nums will contain 
        # only positive numbers.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        # Use index as a hash key and number sign as a presence detector.
        # For example, if nums[1] is negative that means that number `1`
        # is present in the array. 
        # If nums[2] is positive - number 2 is missing.
        for i in range(n): 
            a = abs(nums[i])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])
            
        # Now the index of the first positive number 
        # is equal to first missing positive.
        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return n
            
        return n + 1