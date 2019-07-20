"""
Description:
Given a sorted integer array without duplicates, return the summary of its ranges.

Example1
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

Solution:
模拟题
仔细处理 corner case:
* len = 0
* len = 1
* i = len(nums) - 2
"""


class Solution:
    """
    @param nums:  a sorted integer array without duplicates
    @return: the summary of its ranges
    """
    def summaryRanges(self, nums):
        # Write your code here
        res = []
        l = len(nums)
        if l == 0:
            return res
        start, end = nums[0], nums[0]
        for i in range(len(nums)-1):
            cur = nums[i]
            next = nums[i+1]
            
            if i == len(nums)-2:
                if next == cur + 1:
                    end = next
                    res.append("{}->{}".format(str(start), str(end)))
                    break
                else:
                    end = cur
                    if start != end:
                        res.append("{}->{}".format(str(start), str(end)))
                    else:
                        res.append(str(start))
                    res.append(str(next))
                    end = next
                    break
            
            if next == cur + 1:
                continue
            else:
                end = cur
                if start != end:
                    res.append("{}->{}".format(str(start), str(end)))
                else:
                    res.append(str(start))
                start = next
        
        if start == end:
            res.append(str(start))
        return res
