-- LeetCode 570 · Managers with at Least 5 Direct Reports · Medium
-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
--
-- Pattern : SQL
-- Solved  : 22 May 2026
-- Time    : O(n)
-- Space   : O(1)

SELECT e.name 
FROM employee e 
JOIN employee em ON e.id = em.managerId 
GROUP BY e.id, e.name
HAVING COUNT(e.id) >= 5;
