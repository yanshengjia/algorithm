"""
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.


Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15


Solution:
1. API
2. Non-API
"""


# Call API
import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = datetime.datetime.strptime(date1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(date2, "%Y-%m-%d").date()
        delta =  abs((date1 - date2).days)
        return delta
