"""
Table: Logs

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| log_id        | int     |
+---------------+---------+
id is the primary key for this table.
Each row of this table contains the ID in a log Table.

Since some IDs have been removed from Logs. Write an SQL query to find the start and end number of continuous ranges in table Logs.

Order the result table by start_id.

The query result format is in the following example:

Logs table:
+------------+
| log_id     |
+------------+
| 1          |
| 2          |
| 3          |
| 7          |
| 8          |
| 10         |
+------------+

Result table:
+------------+--------------+
| start_id   | end_id       |
+------------+--------------+
| 1          | 3            |
| 7          | 8            |
| 10         | 10           |
+------------+--------------+
The result table should contain all ranges in table Logs.
From 1 to 3 is contained in the table.
From 4 to 6 is missing in the table
From 7 to 8 is contained in the table.
Number 9 is missing in the table.
Number 10 is contained in the table.


Solution:
Select from derived table:

log_id, num, difference
1, 1, 0
2, 2, 0
3, 3, 0
7, 4, 3
8, 5, 3
10, 6, 4

row_number() + over() -> generate row number
"""


SELECT min(log_id) as start_id, max(log_id) as end_id
FROM
(
    SELECT log_id, ROW_NUMBER() OVER() as num
    FROM Logs
) as diff
GROUP BY log_id - num
