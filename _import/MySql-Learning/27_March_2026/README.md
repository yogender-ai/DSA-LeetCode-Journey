<![CDATA[<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=220&section=header&text=📅%20Day%201%20—%2027%20March%202026&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=MySQL%20Fundamentals%20%7C%20SELECT%20%7C%20WHERE%20%7C%20ORDER%20BY&descSize=16&descAlignY=58&descAlign=50" width="100%" />

<!-- Badges -->
[![MySQL](https://img.shields.io/badge/MySQL-9.6.0-00758f?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![Database](https://img.shields.io/badge/Database-org-blueviolet?style=for-the-badge&logo=databricks&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Completed%20✅-00c853?style=for-the-badge)](#)

---

### 🧠 Topics Covered Today

</div>

| # | Topic | SQL Keyword | Description |
|:-:|:------|:------------|:------------|
| 1 | 🗄️ Database Exploration | `SHOW DATABASES`, `USE`, `SHOW TABLES` | Listing databases and tables |
| 2 | 📋 Basic SELECT | `SELECT *`, `SELECT col` | Retrieving all or specific columns |
| 3 | 🧮 Calculator Mode | `SELECT 44+11`, `SELECT NOW()` | Using MySQL for math & date/time |
| 4 | 🔍 WHERE Clause | `WHERE col = value` | Filtering rows on conditions |
| 5 | 📊 BETWEEN | `BETWEEN ... AND ...` | Range-based filtering (inclusive) |
| 6 | 📝 IN / NOT IN | `IN (...)`, `NOT IN (...)` | Multi-value filtering |
| 7 | 🔎 LIKE (Wildcards) | `LIKE '%pattern%'` | Pattern matching with `%` wildcard |
| 8 | 🔢 ORDER BY | `ORDER BY col ASC\|DESC` | Sorting results |

---

<div align="center">

### ⚡ Quick Reference — Commands Used

</div>

---

#### 📂 Section 1 — Database & Table Exploration

```sql
SHOW DATABASES;
```
```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| org                |
| performance_schema |
| sakila             |
| sys                |
+--------------------+
```

```sql
USE org;
SHOW TABLES;
```
```
+---------------+
| Tables_in_org |
+---------------+
| bonus         |
| title         |
| worker        |
+---------------+
```

---

#### 📋 Section 2 — Basic SELECT Queries

```sql
-- Fetch all records
SELECT * FROM worker;
```
```
+-----------+------------+-----------+--------+---------------------+------------+
| WORKER_ID | FIRST_NAME | LAST_NAME | SALARY | JOINING_DATE        | DEPARTMENT |
+-----------+------------+-----------+--------+---------------------+------------+
|         1 | Monika     | Arora     | 100000 | 2014-02-20 09:00:00 | HR         |
|         2 | Niharika   | Verma     |  80000 | 2014-06-11 09:00:00 | Admin      |
|         3 | Vishal     | Singhal   | 300000 | 2014-02-20 09:00:00 | HR         |
|         4 | Amitabh    | Singh     | 500000 | 2014-02-20 09:00:00 | Admin      |
|         5 | Vivek      | Bhati     | 500000 | 2014-06-11 09:00:00 | Admin      |
|         6 | Vipul      | Diwan     | 200000 | 2014-06-11 09:00:00 | Account    |
|         7 | Satish     | Kumar     |  75000 | 2014-01-20 09:00:00 | Account    |
|         8 | Geetika    | Chauhan   |  90000 | 2014-04-11 09:00:00 | Admin      |
+-----------+------------+-----------+--------+---------------------+------------+
```

```sql
-- Fetch only salary column
SELECT salary FROM worker;
```
```
+--------+
| salary |
+--------+
| 100000 |
|  80000 |
| 300000 |
| 500000 |
| 500000 |
| 200000 |
|  75000 |
|  90000 |
+--------+
```

```sql
-- Fetch only last_name column
SELECT last_name FROM worker;
```
```
+-----------+
| last_name |
+-----------+
| Arora     |
| Verma     |
| Singhal   |
| Singh     |
| Bhati     |
| Diwan     |
| Kumar     |
| Chauhan   |
+-----------+
```

---

#### 🧮 Section 3 — MySQL as a Calculator

```sql
-- Arithmetic expression
SELECT 44 + 11;
```
```
+-------+
| 44+11 |
+-------+
|    55 |
+-------+
```

```sql
-- Current date & time
SELECT NOW();
```
```
+---------------------+
| now()               |
+---------------------+
| 2026-03-27 03:52:39 |
+---------------------+
```

---

#### 🔍 Section 4 — WHERE Clause (Filtering)

```sql
-- Salary greater than 200000
SELECT * FROM worker WHERE salary > 200000;
```
```
+-----------+------------+-----------+--------+---------------------+------------+
| WORKER_ID | FIRST_NAME | LAST_NAME | SALARY | JOINING_DATE        | DEPARTMENT |
+-----------+------------+-----------+--------+---------------------+------------+
|         3 | Vishal     | Singhal   | 300000 | 2014-02-20 09:00:00 | HR         |
|         4 | Amitabh    | Singh     | 500000 | 2014-02-20 09:00:00 | Admin      |
|         5 | Vivek      | Bhati     | 500000 | 2014-06-11 09:00:00 | Admin      |
+-----------+------------+-----------+--------+---------------------+------------+
```

```sql
-- Filter by department (case-insensitive by default)
SELECT * FROM worker WHERE department = 'HR';
SELECT * FROM worker WHERE department = 'hr';   -- same result
SELECT * FROM worker WHERE department = "hr";   -- double quotes also work
```
```
+-----------+------------+-----------+--------+---------------------+------------+
| WORKER_ID | FIRST_NAME | LAST_NAME | SALARY | JOINING_DATE        | DEPARTMENT |
+-----------+------------+-----------+--------+---------------------+------------+
|         1 | Monika     | Arora     | 100000 | 2014-02-20 09:00:00 | HR         |
|         3 | Vishal     | Singhal   | 300000 | 2014-02-20 09:00:00 | HR         |
+-----------+------------+-----------+--------+---------------------+------------+
```

---

#### 📊 Section 5 — BETWEEN (Range Filtering)

```sql
-- Salary between 100000 and 500000 (inclusive)
SELECT * FROM worker WHERE salary BETWEEN 100000 AND 500000;
```
```
+-----------+------------+-----------+--------+---------------------+------------+
| WORKER_ID | FIRST_NAME | LAST_NAME | SALARY | JOINING_DATE        | DEPARTMENT |
+-----------+------------+-----------+--------+---------------------+------------+
|         1 | Monika     | Arora     | 100000 | 2014-02-20 09:00:00 | HR         |
|         3 | Vishal     | Singhal   | 300000 | 2014-02-20 09:00:00 | HR         |
|         4 | Amitabh    | Singh     | 500000 | 2014-02-20 09:00:00 | Admin      |
|         5 | Vivek      | Bhati     | 500000 | 2014-06-11 09:00:00 | Admin      |
|         6 | Vipul      | Diwan     | 200000 | 2014-06-11 09:00:00 | Account    |
+-----------+------------+-----------+--------+---------------------+------------+
```

---

#### 📝 Section 6 — IN & NOT IN

```sql
-- ❌ Longer way with OR
SELECT * FROM worker WHERE department = 'hr' OR department = 'admin';

-- ✅ Cleaner way with IN
SELECT * FROM worker WHERE department IN ('hr', 'admin');
```
```
+-----------+------------+-----------+--------+---------------------+------------+
| WORKER_ID | FIRST_NAME | LAST_NAME | SALARY | JOINING_DATE        | DEPARTMENT |
+-----------+------------+-----------+--------+---------------------+------------+
|         1 | Monika     | Arora     | 100000 | 2014-02-20 09:00:00 | HR         |
|         2 | Niharika   | Verma     |  80000 | 2014-06-11 09:00:00 | Admin      |
|         3 | Vishal     | Singhal   | 300000 | 2014-02-20 09:00:00 | HR         |
|         4 | Amitabh    | Singh     | 500000 | 2014-02-20 09:00:00 | Admin      |
|         5 | Vivek      | Bhati     | 500000 | 2014-06-11 09:00:00 | Admin      |
|         8 | Geetika    | Chauhan   |  90000 | 2014-04-11 09:00:00 | Admin      |
+-----------+------------+-----------+--------+---------------------+------------+
```

```sql
-- NOT IN: Exclude HR and Admin
SELECT * FROM worker WHERE department NOT IN ('hr', 'admin');
```
```
+-----------+------------+-----------+--------+---------------------+------------+
| WORKER_ID | FIRST_NAME | LAST_NAME | SALARY | JOINING_DATE        | DEPARTMENT |
+-----------+------------+-----------+--------+---------------------+------------+
|         6 | Vipul      | Diwan     | 200000 | 2014-06-11 09:00:00 | Account    |
|         7 | Satish     | Kumar     |  75000 | 2014-01-20 09:00:00 | Account    |
+-----------+------------+-----------+--------+---------------------+------------+
```

---

#### 🔎 Section 7 — LIKE (Pattern Matching)

```sql
-- Find first names containing 'vi'
SELECT * FROM worker WHERE first_name LIKE '%vi%';
```
```
+-----------+------------+-----------+--------+---------------------+------------+
| WORKER_ID | FIRST_NAME | LAST_NAME | SALARY | JOINING_DATE        | DEPARTMENT |
+-----------+------------+-----------+--------+---------------------+------------+
|         3 | Vishal     | Singhal   | 300000 | 2014-02-20 09:00:00 | HR         |
|         5 | Vivek      | Bhati     | 500000 | 2014-06-11 09:00:00 | Admin      |
|         6 | Vipul      | Diwan     | 200000 | 2014-06-11 09:00:00 | Account    |
+-----------+------------+-----------+--------+---------------------+------------+
```

---

#### 🔢 Section 8 — ORDER BY (Sorting)

```sql
-- Sort by salary ascending (default)
SELECT * FROM worker ORDER BY salary;
```
```
+-----------+------------+-----------+--------+---------------------+------------+
| WORKER_ID | FIRST_NAME | LAST_NAME | SALARY | JOINING_DATE        | DEPARTMENT |
+-----------+------------+-----------+--------+---------------------+------------+
|         7 | Satish     | Kumar     |  75000 | 2014-01-20 09:00:00 | Account    |
|         2 | Niharika   | Verma     |  80000 | 2014-06-11 09:00:00 | Admin      |
|         8 | Geetika    | Chauhan   |  90000 | 2014-04-11 09:00:00 | Admin      |
|         1 | Monika     | Arora     | 100000 | 2014-02-20 09:00:00 | HR         |
|         6 | Vipul      | Diwan     | 200000 | 2014-06-11 09:00:00 | Account    |
|         3 | Vishal     | Singhal   | 300000 | 2014-02-20 09:00:00 | HR         |
|         4 | Amitabh    | Singh     | 500000 | 2014-02-20 09:00:00 | Admin      |
|         5 | Vivek      | Bhati     | 500000 | 2014-06-11 09:00:00 | Admin      |
+-----------+------------+-----------+--------+---------------------+------------+
```

```sql
-- Sort by salary descending
SELECT * FROM worker ORDER BY salary DESC;
```
```
+-----------+------------+-----------+--------+---------------------+------------+
| WORKER_ID | FIRST_NAME | LAST_NAME | SALARY | JOINING_DATE        | DEPARTMENT |
+-----------+------------+-----------+--------+---------------------+------------+
|         4 | Amitabh    | Singh     | 500000 | 2014-02-20 09:00:00 | Admin      |
|         5 | Vivek      | Bhati     | 500000 | 2014-06-11 09:00:00 | Admin      |
|         3 | Vishal     | Singhal   | 300000 | 2014-02-20 09:00:00 | HR         |
|         6 | Vipul      | Diwan     | 200000 | 2014-06-11 09:00:00 | Account    |
|         1 | Monika     | Arora     | 100000 | 2014-02-20 09:00:00 | HR         |
|         8 | Geetika    | Chauhan   |  90000 | 2014-04-11 09:00:00 | Admin      |
|         2 | Niharika   | Verma     |  80000 | 2014-06-11 09:00:00 | Admin      |
|         7 | Satish     | Kumar     |  75000 | 2014-01-20 09:00:00 | Account    |
+-----------+------------+-----------+--------+---------------------+------------+
```

---

<div align="center">

### 💡 Key Takeaways

| Concept | Syntax | Note |
|:--------|:-------|:-----|
| Select all | `SELECT * FROM table` | `*` = all columns |
| Filter rows | `WHERE condition` | Use `=`, `>`, `<`, `>=`, `<=`, `!=` |
| Range filter | `BETWEEN x AND y` | Inclusive on both ends |
| List match | `IN (val1, val2)` | Cleaner than multiple `OR` |
| Exclude list | `NOT IN (val1, val2)` | Opposite of `IN` |
| Pattern match | `LIKE '%text%'` | `%` = any characters |
| Sort ascending | `ORDER BY col` | Default is `ASC` |
| Sort descending | `ORDER BY col DESC` | Highest first |
| Case sensitivity | Default: **insensitive** | Depends on collation |

---

### ⚠️ Common Mistakes Made Today

| Mistake | Correction |
|:--------|:-----------|
| `SELECT * worker` | Must use `FROM` → `SELECT * FROM worker` |
| `SELECT * FROM worker ORDER BY DESC` | Must specify column → `ORDER BY salary DESC` |
| `SELECT * FROM worker LIKE '%vi%'` | `LIKE` needs `WHERE` + column → `WHERE first_name LIKE '%vi%'` |

---

<br>

> *"The beginning is always today."* — **Mary Shelley**

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=120&section=footer" width="100%" />

</div>
]]>
