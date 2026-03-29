-- ============================================================
-- 📅 MySQL Learning Session — 29 March 2026
-- 🖥️  Server: MySQL 9.6.0 Community Server (GPL)
-- 🗄️  Database: org
-- ============================================================


-- ──────────────────────────────────────────────────────────────
-- 📊 SECTION 1: ADVANCED SORTING (ORDER BY)
-- ──────────────────────────────────────────────────────────────

-- Fetch all workers sorted by salary in ascending order (default)
SELECT * FROM worker ORDER BY salary;

-- Fetch all workers sorted by salary in descending order (highest first)
SELECT * FROM worker ORDER BY salary DESC;


-- ──────────────────────────────────────────────────────────────
-- 📋 SECTION 2: DISTINCT VALUES
-- ──────────────────────────────────────────────────────────────

-- Fetch unique department names from the worker table
-- This removes duplicates and shows only one entry per department.
SELECT DISTINCT department FROM worker;


-- ──────────────────────────────────────────────────────────────
-- 🔢 SECTION 3: GROUP BY & AGGREGATIONS
-- ──────────────────────────────────────────────────────────────

-- Count the number of workers in each department
-- GROUP BY groups results by the specified column, and COUNT() is an aggregate function.
SELECT department, COUNT(department) 
FROM worker 
GROUP BY department;

-- Group by first_name and count occurrences
-- (Since first names are unique in the current dataset, count is 1 for each)
SELECT first_name, COUNT(*) 
FROM worker 
GROUP BY first_name;


-- ============================================================
-- 💡 KEY TAKEAWAYS FROM TODAY'S SESSION:
-- ============================================================
-- 1. ORDER BY col DESC      → Sort results in descending order.
-- 2. SELECT DISTINCT        → Returns only unique (different) values.
-- 3. GROUP BY               → Group rows that have the same values into summary rows.
-- 4. COUNT(*)               → An aggregate function that returns the number of rows.
-- 5. Syntax Tip: Always check table/column names (avoid 'wroker' or 'name' errors).
-- ============================================================
