-- LeetCode 197 · Rising Temperature · Easy
-- https://leetcode.com/problems/rising-temperature/
--
-- Pattern : SQL
-- Solved  : 17 May 2026
-- Time    : O(n)
-- Space   : O(1)

SELECT today.id 
FROM Weather today 
JOIN Weather yes 
  ON yes.recordDate = DATE_SUB(today.recordDate, INTERVAL 1 DAY) 
WHERE yes.temperature < today.temperature;
