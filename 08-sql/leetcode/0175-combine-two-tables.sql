-- LeetCode 175 · Combine Two Tables · Easy
-- https://leetcode.com/problems/combine-two-tables/
-- Solved : 12 Apr 2026

SELECT p.firstName, p.lastName, a.city, a.state 
FROM Person AS p 
LEFT JOIN Address AS a ON p.personId = a.personId;
