-- LeetCode 619 · Biggest Single Number · Easy
-- https://leetcode.com/problems/biggest-single-number/
--
-- Pattern : SQL
-- Solved  : 16 Jul 2026
-- Time    : O(n)
-- Space   : O(1)

select max(num) as num from  (select num from MyNumbers
group by num 
having  count(num)=1
) as t;
