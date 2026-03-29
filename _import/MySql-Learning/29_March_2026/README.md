<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=220&section=header&text=📅%20Day%202%20—%2029%20March%202026&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Advanced%20Sorting%20%7C%20DISTINCT%20%7C%20GROUP%20BY&descSize=16&descAlignY=58&descAlign=50" width="100%" />

<!-- Badges -->
[![MySQL](https://img.shields.io/badge/MySQL-9.6.0-00758f?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![Database](https://img.shields.io/badge/Database-org-blueviolet?style=for-the-badge&logo=databricks&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Completed%20✅-00c853?style=for-the-badge)](#)

---

### 🧠 Topics Covered Today

| # | Topic | Keyword |
|:-:|:------|:--------|
| 1 | 📊 Advanced Sorting | `ORDER BY col DESC` |
| 2 | 📋 Unique Values | `SELECT DISTINCT` |
| 3 | 🔢 Grouping Results | `GROUP BY`, `COUNT(*)` |
| 4 | 🏷️ Aggregate Functions | `COUNT(department)` |

---

</div>

### ⚡ Quick Reference — Commands & Outputs

#### 📊 Advanced Sorting (Descending Order)

```sql
-- Fetch all workers sorted by salary (highest first)
SELECT * FROM worker ORDER BY salary DESC;
```
| WORKER_ID | FIRST_NAME | LAST_NAME | SALARY | JOINING_DATE | DEPARTMENT |
|:----------|:-----------|:----------|:-------|:-------------|:-----------|
| 4 | Amitabh | Singh | 500000 | 2014-02-20 | Admin |
| 5 | Vivek | Bhati | 500000 | 2014-06-11 | Admin |
| 3 | Vishal | Singhal | 300000 | 2014-02-20 | HR |
| 6 | Vipul | Diwan | 200000 | 2014-06-11 | Account |

#### 📋 Fetching Unique Values

```sql
-- Find unique departments
SELECT DISTINCT department FROM worker;
```
| department |
|:-----------|
| HR |
| Admin |
| Account |

#### 🔢 Aggregations with GROUP BY

```sql
-- Count number of workers in each department
SELECT department, COUNT(department) FROM worker GROUP BY department;
```
| department | count(department) |
|:-----------|:------------------|
| HR | 2 |
| Admin | 4 |
| Account | 2 |

---

<div align="center">

### 💡 Key Takeaways

| Concept | Syntax |
|:--------|:-------|
| Sort Descending | `ORDER BY col DESC` |
| Unique Values | `SELECT DISTINCT col` |
| Group Rows | `GROUP BY col` |
| Count Results | `COUNT(*)` |

---

### ⚠️ Mistakes to Avoid

> [!WARNING]
> - **Typo**: `select * wroker` ❌ → `select * from worker` ✅ (Remember the `FROM` keyword!)
> - **Invalid Column**: `count(name)` ❌ when column `name` does not exist → Use `count(*)` or a valid column like `first_name`.
> - **Group By Requirement**: When using `COUNT()`, group by the non-aggregated column (e.g., `department`).

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=120&section=footer" width="100%" />

</div>
