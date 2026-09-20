-- LeetCode 610 · Triangle Judgement · Easy
-- https://leetcode.com/problems/triangle-judgement/
--
-- Pattern : SQL
-- Solved  : 17 Jul 2026
-- Time    : O(n)
-- Space   : O(1)

select x,y,z,
case
when (x+y>z&&y+z>x&&z+x>y) then 'Yes'
else 'No'
end as triangle
from Triangle;
