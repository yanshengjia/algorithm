"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

Solution:
1. Hashtable. Space: O(N)
2. Flip. Space: O(1)
When find a number i, flip the number at position i-1 to negative. 
if the number at position i-1 is already negative, i is the number that occurs twice.
"""


# Flip
# Time: O(N), N is the length of nums
# Space: O(1)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        # flip
        for i in range(len(nums)):
            n = abs(nums[i])
            idx = abs(n-1)
            if nums[idx] < 0:
                res.append(n)
            else:
                nums[idx] *= -1
        return res
