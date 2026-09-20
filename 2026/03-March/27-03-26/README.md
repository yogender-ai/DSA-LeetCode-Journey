<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=220&section=header&text=📅%20Day%201%20—%2027%20March%202026&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=MySQL%20Fundamentals%20%7C%20SELECT%20%7C%20WHERE%20%7C%20ORDER%20BY&descSize=16&descAlignY=58&descAlign=50" width="100%" />

<!-- Badges -->
[![MySQL](https://img.shields.io/badge/MySQL-9.6.0-00758f?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![Database](https://img.shields.io/badge/Database-org-blueviolet?style=for-the-badge&logo=databricks&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Completed%20✅-00c853?style=for-the-badge)](#)

---

### 🧠 Topics Covered Today

| # | Topic | Keyword |
|:-:|:------|:--------|
| 1 | 🗄️ Exploration | `SHOW DATABASES`, `USE`, `SHOW TABLES` |
| 2 | 📋 Basic SELECT | `SELECT *`, `SELECT col` |
| 3 | 🧮 Math/Date | `SELECT 44+11`, `SELECT NOW()` |
| 4 | 🔍 Filtering | `WHERE`, `BETWEEN`, `IN`, `LIKE` |
| 5 | 🔢 Sorting | `ORDER BY col ASC\|DESC` |

---

</div>

### ⚡ Quick Reference — Commands Used

#### 📋 Basic SELECT Queries

```sql
-- Fetch all records
SELECT * FROM worker;
```
| WORKER_ID | FIRST_NAME | LAST_NAME | SALARY | DEPARTMENT |
|:----------|:-----------|:----------|:-------|:-----------|
| 1 | Monika | Arora | 100000 | HR |
| 2 | Niharika | Verma | 80000 | Admin |
| 3 | Vishal | Singhal | 300000 | HR |
| 4 | Amitabh | Singh | 500000 | Admin |

#### 🔍 Filtering (WHERE Clause)

```sql
-- Range Filtering
SELECT * FROM worker WHERE salary BETWEEN 100000 AND 500000;

-- List Matching
SELECT * FROM worker WHERE department IN ('hr', 'admin');

-- Pattern Matching
SELECT * FROM worker WHERE first_name LIKE '%vi%';
```

#### 🔢 Sorting (ORDER BY)

```sql
-- Sort by salary descending
SELECT * FROM worker ORDER BY salary DESC;
```

---

<div align="center">

### 💡 Key Takeaways

| Concept | Syntax |
|:--------|:-------|
| Select all | `SELECT * FROM table` |
| Filter rows | `WHERE condition` |
| Range filter | `BETWEEN x AND y` |
| List match | `IN (val1, val2)` |
| Pattern match | `LIKE '%text%'` |
| Sort results | `ORDER BY col DESC` |

---

### ⚠️ Mistakes to Avoid

> [!WARNING]
> - **Syntax Error**: `SELECT * worker` ❌ → `SELECT * FROM worker` ✅
> - **Sorting**: `ORDER BY DESC` ❌ → `ORDER BY salary DESC` ✅

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=120&section=footer" width="100%" />

</div>
