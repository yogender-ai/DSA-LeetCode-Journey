-- ============================================================
-- 📅 MySQL Learning Session — 09 April 2026
-- 🖥️  Server: MySQL 9.6.0 Community Server (GPL)
-- 🗄️  Database: temp
-- ============================================================


-- ──────────────────────────────────────────────────────────────
-- 📂 SECTION 1: DATABASE CREATION & SWITCHING
-- ──────────────────────────────────────────────────────────────

-- List all databases on the server
SHOW DATABASES;

-- Switch to the 'org' database
USE org;

-- Create a new database called 'temp'
CREATE DATABASE temp;

-- Switch to the newly created 'temp' database
USE temp;


-- ──────────────────────────────────────────────────────────────
-- 🏗️ SECTION 2: CREATE TABLE — Basic & Constraints
-- ──────────────────────────────────────────────────────────────

-- Create a basic 'customer' table with various column types
CREATE TABLE customer (
    id       INTEGER PRIMARY KEY,
    cname    VARCHAR(225),
    address  VARCHAR(255),
    cit      VARCHAR(100),
    pincode  INTEGER
);

-- Verify the table was created
SHOW TABLES;

-- Create an 'account' table with constraints:
--   • PRIMARY KEY on id
--   • UNIQUE on name
--   • CHECK constraint ensuring balance > 1000
CREATE TABLE account (
    id      INT PRIMARY KEY,
    name    VARCHAR(255) UNIQUE,
    balance INT,
    CONSTRAINT acc_balance_chk CHECK (balance > 1000)
);


-- ──────────────────────────────────────────────────────────────
-- 📥 SECTION 3: INSERT & CONSTRAINT VERIFICATION
-- ──────────────────────────────────────────────────────────────

-- Insert a valid row (balance = 10000, passes CHECK)
INSERT INTO account (id, name, balance)
VALUES (1, 'Yash', 10000);

-- Verify the inserted data
SELECT * FROM account;
-- Output:
-- +----+------+---------+
-- | id | name | balance |
-- +----+------+---------+
-- |  1 | Yash |   10000 |
-- +----+------+---------+

-- ❌ This insert FAILS — balance = 100 violates CHECK (balance > 1000)
INSERT INTO account (id, name, balance)
VALUES (2, 'ABC', 100);
-- ERROR 3819: Check constraint 'acc_balance_chk' is violated.


-- ──────────────────────────────────────────────────────────────
-- 🗑️ SECTION 4: DROP TABLE & RECREATE
-- ──────────────────────────────────────────────────────────────

-- Drop the account table entirely
DROP TABLE account;

-- Verify it's gone
SHOW TABLES;

-- Recreate account with only id column (for ALTER TABLE practice)
CREATE TABLE account (
    id INT PRIMARY KEY
);


-- ──────────────────────────────────────────────────────────────
-- ➕ SECTION 5: ALTER TABLE — ADD COLUMN
-- ──────────────────────────────────────────────────────────────

-- Add a new column 'name' to the account table
ALTER TABLE account ADD name VARCHAR(225) NOT NULL;

-- Verify the new column was added
SHOW COLUMNS FROM account;
-- Output:
-- +-------+--------------+------+-----+---------+-------+
-- | Field | Type         | Null | Key | Default | Extra |
-- +-------+--------------+------+-----+---------+-------+
-- | id    | int          | NO   | PRI | NULL    |       |
-- | name  | varchar(225) | NO   |     | NULL    |       |
-- +-------+--------------+------+-----+---------+-------+


-- ──────────────────────────────────────────────────────────────
-- 🔄 SECTION 6: ALTER TABLE — MODIFY COLUMN
-- Modify changes the data type / constraints (keeps the column name)
-- ──────────────────────────────────────────────────────────────

-- Change 'name' from VARCHAR(225) to INT with a default value of 0
ALTER TABLE account MODIFY name INT NOT NULL DEFAULT 0;

-- Verify the modification
DESC account;
-- Output:
-- +-------+------+------+-----+---------+-------+
-- | Field | Type | Null | Key | Default | Extra |
-- +-------+------+------+-----+---------+-------+
-- | id    | int  | NO   | PRI | NULL    |       |
-- | name  | int  | NO   |     | 0       |       |
-- +-------+------+------+-----+---------+-------+


-- ──────────────────────────────────────────────────────────────
-- ✏️ SECTION 7: ALTER TABLE — CHANGE COLUMN (Rename + Modify)
-- CHANGE can rename and change data type simultaneously
-- ──────────────────────────────────────────────────────────────

-- Rename 'name' to 'First_Name' and change type back to VARCHAR(225)
ALTER TABLE account CHANGE COLUMN name First_Name VARCHAR(225);

-- Verify the change
DESC account;
-- Output:
-- +------------+--------------+------+-----+---------+-------+
-- | Field      | Type         | Null | Key | Default | Extra |
-- +------------+--------------+------+-----+---------+-------+
-- | id         | int          | NO   | PRI | NULL    |       |
-- | First_Name | varchar(225) | YES  |     | NULL    |       |
-- +------------+--------------+------+-----+---------+-------+


-- ──────────────────────────────────────────────────────────────
-- ❌ SECTION 8: ALTER TABLE — DROP COLUMN
-- ──────────────────────────────────────────────────────────────

-- Remove the 'First_Name' column from the table
ALTER TABLE account DROP First_Name;

-- Verify the column was removed
DESC account;
-- Output:
-- +-------+------+------+-----+---------+-------+
-- | Field | Type | Null | Key | Default | Extra |
-- +-------+------+------+-----+---------+-------+
-- | id    | int  | NO   | PRI | NULL    |       |
-- +-------+------+------+-----+---------+-------+


-- ──────────────────────────────────────────────────────────────
-- 📛 SECTION 9: ALTER TABLE — RENAME TABLE
-- ──────────────────────────────────────────────────────────────

-- Rename 'account' table to 'tables'
ALTER TABLE account RENAME tables;

-- Verify the rename
SHOW TABLES;
-- Output:
-- +----------------+
-- | Tables_in_temp |
-- +----------------+
-- | customer       |
-- | tables         |
-- +----------------+


-- ============================================================
-- 💡 KEY TAKEAWAYS FROM TODAY'S SESSION:
-- ============================================================
-- 1. CREATE DATABASE db_name      → Creates a new database
-- 2. CREATE TABLE t (...)         → Creates a table with columns & constraints
-- 3. PRIMARY KEY                  → Uniquely identifies each row
-- 4. UNIQUE                       → Prevents duplicate values in a column
-- 5. CHECK (condition)            → Validates data before insertion
-- 6. DROP TABLE t                 → Permanently deletes a table
-- 7. ALTER TABLE t ADD col type   → Adds a new column
-- 8. ALTER TABLE t MODIFY col     → Changes column type/constraints (keeps name)
-- 9. ALTER TABLE t CHANGE old new → Renames column + optionally changes type
-- 10. ALTER TABLE t DROP col      → Removes a column
-- 11. ALTER TABLE t RENAME new    → Renames the entire table
-- 12. DESC table                  → Shortcut for SHOW COLUMNS FROM table
-- ============================================================
