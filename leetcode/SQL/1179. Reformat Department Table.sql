"""
Table: Department

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| revenue       | int     |
| month         | varchar |
+---------------+---------+
(id, month) is the primary key of this table.
The table has information about the revenue of each department per month.
The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].
 

Write an SQL query to reformat the table such that there is a department id column and a revenue column for each month.

The query result format is in the following example:

Department table:
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+

Result table:
+------+-------------+-------------+-------------+-----+-------------+
| id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
+------+-------------+-------------+-------------+-----+-------------+
| 1    | 8000        | 7000        | 6000        | ... | null        |
| 2    | 9000        | null        | null        | ... | null        |
| 3    | null        | 10000       | null        | ... | null        |
+------+-------------+-------------+-------------+-----+-------------+

Note that the result table has 13 columns (1 for the department id + 12 for the months).


Solution:
Group by + MAX
Group by id 之后每个 id 都只有一条记录，需要用 MAX 来 extract id 下每个月的 revenue. HACK!
Because by using GROUP BY sql engine creates a set of result rows for each element in GROUP BY clause and allows only aggregate operations only against multiple values like SUM, AVG, MIN, MAX, COUNT. Since our set consists of one element and we cannot extract this element directly from GROUP BY we are using kind of hack - aggregate function over single element. Aggregate function for one element = this element.
"""


# Write your MySQL query statement below
SELECT 
    id, 
    MAX(CASE WHEN month = 'Jan' THEN revenue ELSE null END) AS Jan_Revenue,
    MAX(CASE WHEN month = 'Feb' THEN revenue ELSE null END) AS Feb_Revenue,
    MAX(CASE WHEN month = 'Mar' THEN revenue ELSE null END) AS Mar_Revenue,
    MAX(CASE WHEN month = 'Apr' THEN revenue ELSE null END) AS Apr_Revenue,
    MAX(CASE WHEN month = 'May' THEN revenue ELSE null END) AS May_Revenue,
    MAX(CASE WHEN month = 'Jun' THEN revenue ELSE null END) AS Jun_Revenue,
    MAX(CASE WHEN month = 'Jul' THEN revenue ELSE null END) AS Jul_Revenue,
    MAX(CASE WHEN month = 'Aug' THEN revenue ELSE null END) AS Aug_Revenue,
    MAX(CASE WHEN month = 'Sep' THEN revenue ELSE null END) AS Sep_Revenue,
    MAX(CASE WHEN month = 'Oct' THEN revenue ELSE null END) AS Oct_Revenue,
    MAX(CASE WHEN month = 'Nov' THEN revenue ELSE null END) AS Nov_Revenue,
    MAX(CASE WHEN month = 'Dec' THEN revenue ELSE null END) AS Dec_Revenue
FROM Department
GROUP BY id