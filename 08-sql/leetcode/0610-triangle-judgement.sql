-- LeetCode 610 · Triangle Judgement · Easy
-- https://leetcode.com/problems/triangle-judgement/
-- Solved : 17 Jul 2026

select x,y,z,
case
when (x+y>z&&y+z>x&&z+x>y) then 'Yes'
else 'No'
end as triangle
from Triangle;
