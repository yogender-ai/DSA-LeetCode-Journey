<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=220&section=header&text=📅%20Day%206%20—%2012%20April%202026&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Joins%20%7C%20INNER%20JOIN%20%7C%20Relationships%20&descSize=16&descAlignY=58&descAlign=50" width="100%" />

<!-- Badges -->
[![MySQL](https://img.shields.io/badge/MySQL-9.6.0-00758f?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![Database](https://img.shields.io/badge/Database-joins-blueviolet?style=for-the-badge&logo=databricks&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Completed%20✅-00c853?style=for-the-badge)](#)

---

### 🧠 Topics Covered Today

| # | Topic | Keyword |
|:-:|:------|:--------|
| 1 | 🔗 Joins | `INNER JOIN` |
| 2 | 📊 Multiple Tables | `FOREIGN KEY` |
| 3 | 🎯 Filtering | `WHERE` clauses with Joins |

---

</div>

### ⚡ Quick Reference — Commands & Outputs

#### 🔗 SQL INNER JOIN Example

The `INNER JOIN` keyword selects records that have matching values in both tables. We created a `joins` database with `employee`, `project`, and `client` tables to practice relational data.

```sql
-- employee id, name, project id, project name 
SELECT e.id, e.fname, e.lname, p.id, p.name 
FROM employee AS e 
INNER JOIN project AS p ON e.id = p.emp_id;

-- employee id, contact detail who are working from delhi with clients based in kolkata
SELECT e.id, e.fname, e.phone_no, e.email_id 
FROM employee AS e 
INNER JOIN client AS c ON e.id = c.emp_id 
WHERE (e.city = 'delhi' AND c.city = 'kolkata');
```

---

<div align="center">

### 💡 Key Takeaways

| Concept | Syntax |
|:--------|:-------|
| Inner Join | `SELECT * FROM table1 INNER JOIN table2 ON table1.col = table2.col;` |
| Aliases | Use `AS` keyword (e.g., `employee AS e`) for shorter, cleaner queries. |

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=120&section=footer" width="100%" />

</div>
