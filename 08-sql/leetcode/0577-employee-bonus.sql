-- LeetCode 577 · Employee Bonus · Easy
-- https://leetcode.com/problems/employee-bonus/
-- Solved : 21 May 2026

SELECT e.name, b.bonus 
FROM employee AS e 
LEFT JOIN bonus AS b ON e.empId = b.empId 
WHERE bonus < 1000 OR bonus IS NULL;
