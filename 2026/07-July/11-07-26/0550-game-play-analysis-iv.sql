-- LeetCode 550 · Game Play Analysis IV · Medium
-- https://leetcode.com/problems/game-play-analysis-iv/
--
-- Pattern : SQL
-- Solved  : 11 Jul 2026
-- Time    : O(n)
-- Space   : O(1)

select round(count(distinct b.player_id)*1.0/count(a.player_id),2)
as fraction

from
(select player_id,min(event_date) as f
    from activity
    group by player_id
) a
left join activity b on a.player_id=b.player_id and b.event_date=a.f+interval 1 day;
