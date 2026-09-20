-- LeetCode 620 · Not Boring Movies · Easy
-- https://leetcode.com/problems/not-boring-movies/
--
-- Pattern : SQL
-- Solved  : 18 Apr 2026
-- Time    : O(n)
-- Space   : O(1)

SELECT id, movie, description, rating 
FROM cinema 
WHERE id % 2 != 0 AND description != 'boring'
ORDER BY rating DESC;
