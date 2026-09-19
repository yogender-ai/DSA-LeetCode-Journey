-- LeetCode 1661 · Average Time of Process per Machine · Easy
-- https://leetcode.com/problems/average-time-of-process-per-machine/
-- Solved : 21 May 2026

SELECT machine_id, 
       ROUND(AVG(CASE WHEN activity_type = 'end' THEN timestamp END) - 
             AVG(CASE WHEN activity_type = 'start' THEN timestamp END), 3) AS processing_time 
FROM activity 
GROUP BY machine_id;
