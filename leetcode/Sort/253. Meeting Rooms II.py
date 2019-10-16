"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1


Solution:
1. Treemap

2. Minheap
Use a minheap to maintain end time of all intervals.
When we process a new interval, compare begin time of current interval with the topmost ele of heap, if cur_begin_time >= smallest_end_time, it means the room of topmost ele can be reused. Otherwise, we allocate a new room.
Pay attention, sort the intervals by beginning time at first. 先来的会议先处理。

3. Chronological Ordering
Treat start time and end time individually! Because
When we encounter an ending event, that means that some meeting that started earlier has ended now. We are not really concerned with which meeting has ended. All we need is that some meeting ended thus making a room available.

Use two arrays to store start timings and end timings. Sort them separately. Use two pointers s_ptr, e_ptr to go through two arrays.
If start[s_ptr] < end[e_ptr], it means no meeting has ended by the time of meeting with s_ptr is to start. So allocate a new room.
If start[s_ptr] >= end[e_ptr], it means some meeting has ended thus we can reuse that room. e_ptr += 1
"""


# Minheap
# Time: O(NlogN), sorting costs O(NlogN), maintaining the heap has N push operations in any case, So it costs O(NlogN)
# Space: O(N), in the worst case all the intervals collide, minheap has N elements
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        
        res = 1
        rooms = []  # minheap
        intervals = sorted(intervals, key=lambda k:k[0])    # sort the intervals by start time
        heapq.heappush(rooms, intervals[0][1])  # push the first interval's end time into minheap
        for i in range(1, len(intervals)):
            samllest_end_time = rooms[0]
            cur_start_time, cur_end_time = intervals[i][0], intervals[i][1]
            if cur_start_time >= samllest_end_time: # reuse the room
                heapq.heappop(rooms)
                heapq.heappush(rooms, cur_end_time)
            else:   # allocate a new room
                res += 1
                heapq.heappush(rooms, cur_end_time)
        return res


# Chronological Ordering
# Time: O(NlogN), sorting OlogN, at most N comparsion
# Space: O(N)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        
        res = 0
        start = [i[0] for i in intervals]
        end = [i[1] for i in intervals]
        start.sort()
        end.sort()
        
        s_ptr, e_ptr = 0, 0
        while s_ptr < len(start) and e_ptr < len(end):
            if start[s_ptr] < end[e_ptr]:   # no meeting has ended at the time s_ptr meeting is to start
                res += 1
                s_ptr += 1
            else:   # an earlier meeting ended, reuse the room
                s_ptr += 1
                e_ptr += 1
        return res
                
        