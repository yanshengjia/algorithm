"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.


Follow up:
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.


Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]


Solution:
For each number i in nums,
we mark the number that i points as negative.
Then we filter the list, get all the indexes
who points to a positive number.
Since those indexes are not visited.
将 nums 中数字i看做下标，将 nums[abs(nums[i])-1] 标记为负。
再次遍历nums数组，正数的下标(+1)就是 missing nums.
"""


# Time: O(N), where N is the length of nums
# Space: O(i), assume the returned list does not count as extra space.
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] *= -1
        
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res
        