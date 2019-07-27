"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]


Solution:
Hash Table
sorted_d = sorted(d.items(), key=lambda kv:kv[1], reverse=True)
"""


# time-O(n+k), where n is the length of list nums
# space-O(m+k), where m is the number of unique numbers in list nums
class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
    """
    def topKFrequent(self, nums, k):
        # Write your code here
        if k == 0:
            return []
        d = dict()
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        sorted_d = sorted(d.items(), key=lambda kv:kv[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sorted_d[i][0])
        return res
