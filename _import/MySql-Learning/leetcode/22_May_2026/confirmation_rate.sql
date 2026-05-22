# Write your MySQL query statement below
SELECT s.user_id, 
       ROUND(IFNULL((COUNT(CASE WHEN c.action = 'confirmed' THEN action END)) / (COUNT(action)), 0), 2) AS confirmation_rate 
FROM signups s 
LEFT JOIN confirmations c ON s.user_id = c.user_id 
GROUP BY s.user_id 
ORDER BY confirmation_rate;
