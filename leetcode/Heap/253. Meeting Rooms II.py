"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1


Solution:
Sort + Priority Queue
Sort the intervals by start time.
Build a Min heap with the end time of intervals.
If the heap top is smaller than start time of new incoming interval, it means we can free that room.
"""


# Heap
# Time: O(NlogN), sorting takes O(NlogN), extract-min operation on a heap takes O(logN).
# Space: O(N) at worst case
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        
        intervals.sort(key=lambda x:x[0])  # sort by start time
        rooms = []  # min-heap, keep track of end time of intervals
        
        heapq.heappush(rooms, intervals[0][1])
        
        for i in range(1, len(intervals)):
            if rooms[0] <= intervals[i][0]:
                # rooms[0] is free
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, intervals[i][1])
        return len(rooms)
        