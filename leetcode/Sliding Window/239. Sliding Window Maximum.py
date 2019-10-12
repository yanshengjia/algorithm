"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?


Solution:
1. Brute Force
2. MaxHeap
3. Deque
4. DP
"""


# Brute Force
# Time: O(Nk), where N is the length of nums
# Space: O(N-k+1), for the output array
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i+k]))
        return res


# MaxHeap
# Time: O(N*(1+logk+klogk)) = O(nklogk), O(1) for remove, O(logk) for heappush, O(klogk) for heapify for each sliding window
# Space: O(N)
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        res = []
        h = []
        heapq.heapify(h)
        
        for i in range(len(nums)):
            if len(h) < k:
                heapq.heappush(h, -nums[i])
                if len(h) == k:
                    res.append(-h[0])
            else:
                h.remove(-nums[i-k])    # destroy the heap structure, need to heapify again
                heapq.heapify(h)
                heapq.heappush(h, -nums[i])
                res.append(-h[0])
        return res


# Deque, maintain the deque each time we insert a ele
# Time: O(N), since each ele is processed exactly twice, it's index added and then removed from the deque
# Space: O(N), since O(N-K+1) is for the output array and O(k) for a deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        window, res = [], []
        for i, x in enumerate(nums):
            if i >= k and window[0] == i - k:   # clear outdated element
                window.pop(0)
            while window and nums(window[-1]) < x:  # if a older element in window is smaller than x, remove it since it can not be the max one in the window
                window.pop()
            window.append(i)
            if i >= k -1:   # generate res
                res.append(nums[window[0]]) # the leftmost ele of window is biggest in the window
        return res
