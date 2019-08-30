"""
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)


Example
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
Related Problems
DifficultyMedium
Total Accepted1442
Total Submitted2621
Accepted Rate54%
 Show Tags
Array
 Company


Solution:
1. Use a list to store all the bookings. Run a linear time search algorithm. 如果两个区间的起始时间中的较大值小于结束区间的较小值，那么就有重合，返回false。
2. Use a map to store all the bookings. Optimize search complexity. 保持 map 中区间是有序的，然后对于新进来的区间，我们在已有区间中查找第一个不小于新入区间的起始时间的区间，将新区间和该区间，该区间的前一个区间进行比较。
Approach 2 refer to 1065.cpp
"""


# List
# > 60%
# Time: O(N), where N is the number of bookings
# Space: O(N)
class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if len(self.calendar) == 0:
            self.calendar.append((start, end))
            return True
        else:
            for book in self.calendar:
                s, e = book[0], book[1]
                if s <= start < e or s < end <= e or (start <= s and end >= e):
                    return False
            self.calendar.append((start, end))
            return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


# List
# > 20%
class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if len(self.calendar) == 0:
            self.calendar.append((start, end))
            return True
        else:
            for book in self.calendar:
                s, e = book[0], book[1]
                if max(s, start) < min(e, end):
                    return False
            self.calendar.append((start, end))
            return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
