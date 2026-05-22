# Write your MySQL query statement below
SELECT p.project_id, 
       ROUND(SUM(e.experience_years) / COUNT(p.employee_id), 2) AS average_years
FROM project p 
JOIN employee e ON p.employee_id = e.employee_id 
GROUP BY p.project_id;
