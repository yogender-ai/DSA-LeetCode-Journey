-- LeetCode 1070 · Product Sales Analysis III · Medium
-- https://leetcode.com/problems/product-sales-analysis-iii/
--
-- Pattern : SQL
-- Solved  : 14 Jul 2026
-- Time    : O(n)
-- Space   : O(1)

select p.product_id, m.first_year ,p.quantity,p.price
from sales p



join(select product_id , min(year) as first_year from sales group by product_id) m
 on m.product_id =p.product_id and m.first_year=p.year;
