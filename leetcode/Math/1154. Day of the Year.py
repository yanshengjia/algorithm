"""
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
Example 3:

Input: date = "2003-03-01"
Output: 60
Example 4:

Input: date = "2004-03-01"
Output: 61


Solution:
Parse and sum up.
Pay attention to leap year.
"""


# Time: O(1)
# Space: O(1)
class Solution:
    def dayOfYear(self, date: str) -> int:
        ymd = date.split('-')
        year = int(ymd[0])
        month = int(ymd[1])
        day = int(ymd[2])
        
        if((year%4 == 0 and year%100 != 0) or year%400 == 0):
            m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        day_number = sum(m[:(month-1)]) + day
        return day_number
