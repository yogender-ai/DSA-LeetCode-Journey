-- LeetCode 584 · Find Customer Referee · Easy
-- https://leetcode.com/problems/find-customer-referee/
--
-- Pattern : SQL
-- Solved  : 18 Apr 2026
-- Time    : O(n)
-- Space   : O(1)

SELECT name 
FROM Customer 
WHERE referee_id != 2 OR referee_id IS NULL;
