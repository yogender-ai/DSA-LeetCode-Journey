-- ============================================================
-- 📅 MySQL Learning Session — 27 March 2026
-- 🖥️  Server: MySQL 9.6.0 Community Server (GPL)
-- 🗄️  Database: org
-- ============================================================


-- ──────────────────────────────────────────────────────────────
-- 📂 SECTION 1: DATABASE & TABLE EXPLORATION
-- ──────────────────────────────────────────────────────────────

-- List all databases available on the server
SHOW DATABASES;

-- Switch to the 'org' database for this session
USE org;

-- List all tables inside the 'org' database
SHOW TABLES;


-- ──────────────────────────────────────────────────────────────
-- 📋 SECTION 2: BASIC SELECT QUERIES
-- ──────────────────────────────────────────────────────────────

-- Fetch all records from the worker table (all columns)
SELECT * FROM worker;

-- Fetch only the salary column from the worker table
SELECT salary FROM worker;

-- Fetch only the last_name column from the worker table
SELECT last_name FROM worker;


-- ──────────────────────────────────────────────────────────────
-- 🧮 SECTION 3: USING MySQL AS A CALCULATOR
-- ──────────────────────────────────────────────────────────────

-- MySQL can evaluate arithmetic expressions directly
SELECT 44 + 11;
-- Output: 55

-- Get the current date and time from the server
SELECT NOW();


-- ──────────────────────────────────────────────────────────────
-- 🔍 SECTION 4: WHERE CLAUSE — FILTERING ROWS
-- ──────────────────────────────────────────────────────────────

-- Filter workers with salary greater than 200000
SELECT * FROM worker WHERE salary > 200000;

-- Filter workers who belong to the 'HR' department
-- NOTE: MySQL string comparison is case-insensitive by default (depends on collation)
SELECT * FROM worker WHERE department = 'HR';

-- Same query with lowercase 'hr' — still works due to case-insensitive collation
SELECT * FROM worker WHERE department = 'hr';

-- Double quotes also work for string values in MySQL (but single quotes are standard SQL)
SELECT * FROM worker WHERE department = "hr";


-- ──────────────────────────────────────────────────────────────
-- 📊 SECTION 5: BETWEEN — RANGE-BASED FILTERING
-- ──────────────────────────────────────────────────────────────

-- Fetch workers with salary between 100000 and 500000 (inclusive on both ends)
SELECT * FROM worker WHERE salary BETWEEN 100000 AND 500000;


-- ──────────────────────────────────────────────────────────────
-- 📝 SECTION 6: IN & NOT IN — MULTI-VALUE FILTERING
-- ──────────────────────────────────────────────────────────────

-- ❌ Longer way: Using multiple OR conditions
SELECT * FROM worker WHERE department = 'hr' OR department = 'admin';

-- ✅ Better way: Using IN operator (cleaner and scalable)
SELECT * FROM worker WHERE department IN ('hr', 'admin');

-- NOT IN: Fetch workers NOT in HR or Admin departments
SELECT * FROM worker WHERE department NOT IN ('hr', 'admin');


-- ──────────────────────────────────────────────────────────────
-- 🔎 SECTION 7: LIKE — PATTERN MATCHING
-- ──────────────────────────────────────────────────────────────

-- Fetch all columns for the first_name column (to see what we're matching against)
SELECT first_name FROM worker;

-- Find workers whose first name contains 'vi' anywhere
-- '%' is a wildcard that matches zero or more characters
SELECT * FROM worker WHERE first_name LIKE '%vi%';


-- ──────────────────────────────────────────────────────────────
-- 🔢 SECTION 8: ORDER BY — SORTING RESULTS
-- ──────────────────────────────────────────────────────────────

-- Sort workers by salary in ascending order (ASC is the default)
SELECT * FROM worker ORDER BY salary;

-- Sort workers by salary in descending order (highest salary first)
SELECT * FROM worker ORDER BY salary DESC;


-- ============================================================
-- 💡 KEY TAKEAWAYS FROM TODAY'S SESSION:
-- ============================================================
-- 1. SELECT * FROM table      → Fetches all rows & columns
-- 2. WHERE                    → Filters rows based on conditions
-- 3. BETWEEN ... AND ...      → Range filter (inclusive)
-- 4. IN (...)                 → Match against a list of values
-- 5. NOT IN (...)             → Exclude a list of values
-- 6. LIKE '%pattern%'         → Wildcard pattern matching
-- 7. ORDER BY col ASC|DESC    → Sort results
-- 8. MySQL is case-insensitive for string comparisons (default)
-- 9. SELECT can evaluate math expressions like a calculator
-- ============================================================
