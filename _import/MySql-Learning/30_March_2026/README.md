<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=220&section=header&text=📅%20Day%203%20—%2030%20March%202026&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Aggregation%20Functions%20%7C%20HAVING%20Clause&descSize=16&descAlignY=58&descAlign=50" width="100%" />

<!-- Badges -->
[![MySQL](https://img.shields.io/badge/MySQL-9.6.0-00758f?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![Database](https://img.shields.io/badge/Database-org-blueviolet?style=for-the-badge&logo=databricks&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Completed%20✅-00c853?style=for-the-badge)](#)

---

### 🧠 Topics Covered Today

| # | Topic | Keyword |
|:-:|:------|:--------|
| 1 | 📈 Aggregation Functions | `AVG()`, `MIN()`, `SUM()`, `MAX()`, `COUNT()` |
| 2 | 📂 Grouping Results | `GROUP BY` |
| 3 | 🔍 Filtering Groups | `HAVING` |
| 4 | 📋 Data Retrieval | `SELECT *` |

---

</div>

### ⚡ Quick Reference — Commands & Outputs

#### 📈 Aggregation & Grouping

```sql
-- Average salary per department
SELECT department, AVG(salary) FROM worker GROUP BY department;
```
| department | avg(salary) |
|:-----------|:------------|
| HR         | 200000.0000 |
| Admin      | 292500.0000 |
| Account    | 137500.0000 |

```sql
-- Minimum salary per department
SELECT department, MIN(salary) FROM worker GROUP BY department;
```
| department | min(salary) |
|:-----------|:------------|
| HR         | 100000      |
| Admin      | 80000       |
| Account    | 75000       |

#### 🔍 Filtering Groups with HAVING

```sql
-- Fetch departments with more than 2 workers
SELECT department, COUNT(department) FROM worker GROUP BY department HAVING COUNT(department) > 2;
```
| department | count(department) |
|:-----------|:------------------|
| Admin      | 4                 |

---

<div align="center">

### 💡 Key Takeaways

| Concept | Description |
|:--------|:------------|
| **MIN / MAX** | Returns lowest / highest value in a column |
| **AVG / SUM** | Computes average / total sum of numerical values |
| **COUNT** | Counts total number of rows or non-null values |
| **HAVING** | Used to filter results *after* grouping (unlike `WHERE`) |

---

### ⚠️ Mistakes to Avoid

> [!WARNING]
> - **Syntax Error**: `show * from worker` ❌ → `select * from worker` ✅ (Remember `SHOW` is for metadata like databases/tables!)
> - **Typo in Keyword**: `group by deparment` ❌ → `group by department` ✅ (Check your spelling!)
> - **Missing Comma**: `select department count(department)` ❌ → `select department, count(department)` ✅ (Columns must be separated!)
> - **WHERE vs HAVING**: Remember that `WHERE` filters rows *before* grouping, while `HAVING` filters groups *after* `GROUP BY`.

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=120&section=footer" width="100%" />

</div>
