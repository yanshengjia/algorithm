"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


Solution:
1. Heap
build a hashmap based on num: frequency, then build a heap based on (-frequency, num), heappop k times
2. Hashtable
build a hashmap num: frequency, sort it, return the first k elements.
"""


# Heap
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        h = [(-f,v) for v,f in c.items()]
        heapq.heapify(h)
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        return res


# Heap
# Time complexity : O(Nlog(k)). The complexity of Counter method is O(N). To build a heap and output list takes (Nlog(k)). Hence the overall complexity of the algorithm is O(N+Nlog(k))=O(Nlog(k)).
# Space complexity : O(N) to store the hash map.
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get)


# Hashmap + Sort
# Time: O(N + NlogN) = O(NlogN)
# Space: O(N) at the worst case, that every num in nums is unique
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = dict()
        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        sorted_d = sorted(d.items(), key=lambda kv:kv[1], reverse=True)
        
        res = []
        for i in range(k):
            res.append(sorted_d[i][0])
        return res