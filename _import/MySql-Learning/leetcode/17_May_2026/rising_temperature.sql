# Write your MySQL query statement below
SELECT today.id 
FROM Weather today 
JOIN Weather yes 
  ON yes.recordDate = DATE_SUB(today.recordDate, INTERVAL 1 DAY) 
WHERE yes.temperature < today.temperature;
