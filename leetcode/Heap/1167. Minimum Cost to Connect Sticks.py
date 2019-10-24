"""
You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.


Example 1:

Input: sticks = [2,4,3]
Output: 14
Example 2:

Input: sticks = [1,8,3,5]
Output: 30


Solution:
Minheap
Everytime we pop 2 smallest elements from the heap and then push their sum into heap, until the size of heap == 1
"""


# Time: O(nlogn)
# Space: O(n), where n is the size of sticks
import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)    # min-heap
        res = 0
        while len(sticks) > 1:
            first = heapq.heappop(sticks)   # O(1)
            second = heapq.heappop(sticks)  # O(1)
            cost = first + second
            res += cost
            heapq.heappush(sticks, cost)    # O(logn)
        return res
