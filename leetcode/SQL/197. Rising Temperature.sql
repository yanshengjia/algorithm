"""
Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.

+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
For example, return the following Ids for the above Weather table:

+----+
| Id |
+----+
|  2 |
|  4 |
+----+


Solution:
Join + Datadiff
"""

# Write your MySQL query statement below
SELECT
    weather.id AS 'Id'
FROM
    weather
        JOIN
    weather w ON DATEDIFF(weather.Recorddate, w.Recorddate) = 1
        AND weather.Temperature > w.Temperature


SELECT DISTINCT a.Id
FROM Weather a,Weather b
WHERE a.Temperature > b.Temperature
AND DATEDIFF(a.Recorddate, b.Recorddate) = 1
