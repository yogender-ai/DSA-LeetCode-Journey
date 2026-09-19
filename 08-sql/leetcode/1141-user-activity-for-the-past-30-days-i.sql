-- LeetCode 1141 · User Activity for the Past 30 Days I · Easy
-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/
-- Solved : 12 Jul 2026

select activity_date as day,  count(distinct user_id) as active_users from
activity
where activity_date between '2019-06-28' AND '2019-07-27' 
GROUP BY activity_date;
