# Write your MySQL query statement below
SELECT machine_id, 
       ROUND(AVG(CASE WHEN activity_type = 'end' THEN timestamp END) - 
             AVG(CASE WHEN activity_type = 'start' THEN timestamp END), 3) AS processing_time 
FROM activity 
GROUP BY machine_id;
