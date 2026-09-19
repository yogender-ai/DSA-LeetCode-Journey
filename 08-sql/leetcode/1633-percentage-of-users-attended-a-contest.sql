-- LeetCode 1633 · Percentage of Users Attended a Contest · Easy
-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/
-- Solved : 22 May 2026

SELECT r.contest_id, 
       ROUND(COUNT(u.user_id) / (SELECT COUNT(user_id) FROM users) * 100, 2) AS percentage 
FROM users u 
RIGHT JOIN register r ON u.user_id = r.user_id
GROUP BY r.contest_id 
ORDER BY percentage DESC, r.contest_id ASC;
