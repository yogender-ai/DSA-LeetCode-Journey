-- LeetCode 181 · Employees Earning More Than Their Managers · Easy
-- https://leetcode.com/problems/employees-earning-more-than-their-managers/
-- Solved : 18 Apr 2026

SELECT e.name AS Employee 
FROM Employee AS e 
JOIN Employee m ON e.managerId = m.id 
WHERE e.salary > m.salary;
