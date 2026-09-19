-- 30 March 2026 SQL Practice

-- 1. Show databases
SHOW DATABASES;

-- 2. Use the 'org' database
USE org;

-- 3. Show tables in the current database
SHOW TABLES;

-- 4. Calculate average salary per department
SELECT department, AVG(salary) FROM worker GROUP BY department;

-- 5. Calculate minimum salary per department
SELECT department, MIN(salary) FROM worker GROUP BY department;

-- 6. Basic data retrieval
SELECT * FROM worker;

-- 7. Using GROUP BY with HAVING clause to filter groups
-- Fetch departments that have more than 2 workers
SELECT department, COUNT(department) FROM worker GROUP BY department HAVING COUNT(department) > 2;
