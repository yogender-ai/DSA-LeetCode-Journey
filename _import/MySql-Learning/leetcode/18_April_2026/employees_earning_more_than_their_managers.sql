# Write your MySQL query statement below
SELECT e.name AS Employee 
FROM Employee AS e 
JOIN Employee m ON e.managerId = m.id 
WHERE e.salary > m.salary;
