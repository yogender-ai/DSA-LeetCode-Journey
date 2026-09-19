-- LeetCode 619 · Biggest Single Number · Easy
-- https://leetcode.com/problems/biggest-single-number/
-- Solved : 16 Jul 2026

select max(num) as num from  (select num from MyNumbers
group by num 
having  count(num)=1
) as t;
