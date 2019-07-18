"""
Description:
Given an array of integers, your task is to count the number of duplicate array elements. Duplicate is defined as two or more identical elements. For example, in the array[1, 2, 2, 3, 3, 3],the two twos are one duplicate and so are the three threes.you need return an integer denoting the number of non-unique(duplicate) values in the numbers array.

Solution:
用一个 dict 记录每个数字出现的次数，留下出现次数大于等于2的数字
结果数组要求顺序，和原数组中数字出现顺序一致
"""


class Solution:
    """
    @param nums: a integer array
    @return: return an integer denoting the number of non-unique(duplicate) values
    """
    def CountDuplicates(self, nums):
        # write your code here
        d = dict()
        res = []
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
                if num not in res:
                    res.append(num)
        return res