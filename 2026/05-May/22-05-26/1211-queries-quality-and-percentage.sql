-- LeetCode 1211 · Queries Quality and Percentage · Easy
-- https://leetcode.com/problems/queries-quality-and-percentage/
--
-- Pattern : SQL
-- Solved  : 22 May 2026
-- Time    : O(n)
-- Space   : O(1)

SELECT query_name, 
       ROUND(SUM(rating / position) / COUNT(position), 2) AS quality, 
       ROUND(COUNT(CASE WHEN rating < 3 THEN 1 ELSE NULL END) / COUNT(rating) * 100, 2) AS poor_query_percentage 
FROM queries 
GROUP BY query_name;
