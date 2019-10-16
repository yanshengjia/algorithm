"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true


Solution:
Sort the list of intervals by start time.
Check if there is an overlap between two intervals.
"""


# Sorting
# Time: O(NlogN), >99%, where N is the lenght og intervals
# Space: O(N)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda k:k[0])
        end = - float('inf')
        for i in sorted_intervals:
            if i[0] >= end:
                end = i[1]
            else:
                return False
        return True


# Sorting
# Time: O(NlogN), >6%, where N is the lenght og intervals
# Space: O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda k:k[0])
        end = - float('inf')
        for i in intervals:
            if i[0] >= end:
                end = i[1]
            else:
                return False
        return True