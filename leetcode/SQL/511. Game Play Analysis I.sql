# Write your MySQL query statement below
# as 创建 min(event_date) 列的别名，使可读性更强
# group by 聚合相同的 player_id
select player_id, min(event_date) as first_login
from Activity 
group by player_id