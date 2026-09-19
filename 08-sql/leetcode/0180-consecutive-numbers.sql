-- LeetCode 180 · Consecutive Numbers · Medium
-- https://leetcode.com/problems/consecutive-numbers/
-- Solved : 17 Jul 2026

select distinct num as ConsecutiveNums from 
(select id,num , lag(num,1) over (order by id) as prev1,
lag (num,2) over (order by id) as prev2 
from Logs) t 
where t.num=t.prev1 and t.prev1=t.prev2;
