-- LeetCode 577 · Employee Bonus · Easy
-- https://leetcode.com/problems/employee-bonus/
--
-- Pattern : SQL
-- Solved  : 21 May 2026
-- Time    : O(n)
-- Space   : O(1)

SELECT e.name, b.bonus 
FROM employee AS e 
LEFT JOIN bonus AS b ON e.empId = b.empId 
WHERE bonus < 1000 OR bonus IS NULL;
