-- LeetCode 1251 · Average Selling Price · Easy
-- https://leetcode.com/problems/average-selling-price/
--
-- Pattern : SQL
-- Solved  : 22 May 2026
-- Time    : O(n)
-- Space   : O(1)

SELECT p.product_id, 
       IFNULL(ROUND(SUM(u.units * p.price) / SUM(units), 2), 0) AS average_price 
FROM prices p 
LEFT JOIN UnitsSold u ON p.product_id = u.product_id 
                      AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;
