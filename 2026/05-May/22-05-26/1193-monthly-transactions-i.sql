-- LeetCode 1193 · Monthly Transactions I · Medium
-- https://leetcode.com/problems/monthly-transactions-i/
--
-- Pattern : SQL
-- Solved  : 22 May 2026
-- Time    : O(n)
-- Space   : O(1)

SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, 
       country, 
       COUNT(amount) AS trans_count, 
       COUNT(CASE WHEN state = 'approved' THEN amount END) AS approved_count, 
       SUM(amount) AS trans_total_amount, 
       IFNULL(SUM(CASE WHEN state = 'approved' THEN amount END), 0) AS approved_total_amount 
FROM transactions
GROUP BY DATE_FORMAT(trans_date, '%Y-%m'), country;
