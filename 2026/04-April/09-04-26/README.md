<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=220&section=header&text=📅%20Day%204%20—%2009%20April%202026&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=DDL%20%7C%20CREATE%20%7C%20ALTER%20%7C%20DROP%20%7C%20Constraints&descSize=16&descAlignY=58&descAlign=50" width="100%" />

<!-- Badges -->
[![MySQL](https://img.shields.io/badge/MySQL-9.6.0-00758f?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![Database](https://img.shields.io/badge/Database-temp-blueviolet?style=for-the-badge&logo=databricks&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Completed%20✅-00c853?style=for-the-badge)](#)

---

### 🧠 Topics Covered Today

| # | Topic | Keyword |
|:-:|:------|:--------|
| 1 | 🗄️ Database Creation | `CREATE DATABASE`, `USE` |
| 2 | 🏗️ Table Creation | `CREATE TABLE`, `PRIMARY KEY`, `UNIQUE`, `CHECK` |
| 3 | 📥 Insert & Constraints | `INSERT INTO`, constraint violations |
| 4 | 🗑️ Drop Table | `DROP TABLE` |
| 5 | ➕ Add Column | `ALTER TABLE ... ADD` |
| 6 | 🔄 Modify Column | `ALTER TABLE ... MODIFY` |
| 7 | ✏️ Change Column | `ALTER TABLE ... CHANGE` |
| 8 | ❌ Drop Column | `ALTER TABLE ... DROP` |
| 9 | 📛 Rename Table | `ALTER TABLE ... RENAME` |

---

</div>

### ⚡ Quick Reference — Commands & Outputs

#### 🏗️ Creating Tables with Constraints

```sql
-- Table with PRIMARY KEY, UNIQUE, and CHECK constraint
CREATE TABLE account (
    id      INT PRIMARY KEY,
    name    VARCHAR(255) UNIQUE,
    balance INT,
    CONSTRAINT acc_balance_chk CHECK (balance > 1000)
);
```

```sql
-- ✅ Valid insert (balance > 1000)
INSERT INTO account (id, name, balance) VALUES (1, 'Yash', 10000);

-- ❌ Fails CHECK constraint (balance = 100)
INSERT INTO account (id, name, balance) VALUES (2, 'ABC', 100);
-- ERROR 3819: Check constraint 'acc_balance_chk' is violated.
```

#### ➕ ALTER TABLE — Add Column

```sql
ALTER TABLE account ADD name VARCHAR(225) NOT NULL;
```
| Field | Type | Null | Key | Default |
|:------|:-----|:-----|:----|:--------|
| id | int | NO | PRI | NULL |
| name | varchar(225) | NO | | NULL |

#### 🔄 ALTER TABLE — Modify Column (change type/constraints, keep name)

```sql
ALTER TABLE account MODIFY name INT NOT NULL DEFAULT 0;
```
| Field | Type | Null | Key | Default |
|:------|:-----|:-----|:----|:--------|
| id | int | NO | PRI | NULL |
| name | int | NO | | 0 |

#### ✏️ ALTER TABLE — Change Column (rename + change type)

```sql
ALTER TABLE account CHANGE COLUMN name First_Name VARCHAR(225);
```
| Field | Type | Null | Key | Default |
|:------|:-----|:-----|:----|:--------|
| id | int | NO | PRI | NULL |
| First_Name | varchar(225) | YES | | NULL |

#### ❌ ALTER TABLE — Drop Column

```sql
ALTER TABLE account DROP First_Name;
```

#### 📛 ALTER TABLE — Rename Table

```sql
ALTER TABLE account RENAME tables;
```

---

<div align="center">

### 💡 Key Takeaways

| Concept | Syntax |
|:--------|:-------|
| Create Database | `CREATE DATABASE db_name` |
| Create Table | `CREATE TABLE t (col TYPE constraints)` |
| Primary Key | `col TYPE PRIMARY KEY` |
| Unique | `col TYPE UNIQUE` |
| Check Constraint | `CONSTRAINT name CHECK (condition)` |
| Drop Table | `DROP TABLE table_name` |
| Add Column | `ALTER TABLE t ADD col TYPE` |
| Modify Column | `ALTER TABLE t MODIFY col NEW_TYPE` |
| Change Column | `ALTER TABLE t CHANGE old_name new_name TYPE` |
| Drop Column | `ALTER TABLE t DROP col` |
| Rename Table | `ALTER TABLE t RENAME new_name` |
| Describe Table | `DESC table_name` |

---

### 🔑 MODIFY vs CHANGE — What's the Difference?

| Feature | `MODIFY` | `CHANGE` |
|:--------|:---------|:---------|
| Rename column? | ❌ No | ✅ Yes |
| Change data type? | ✅ Yes | ✅ Yes |
| Change constraints? | ✅ Yes | ✅ Yes |

---

### ⚠️ Mistakes to Avoid

> [!WARNING]
> - **Typo**: `shwo databases` ❌ → `SHOW DATABASES` ✅
> - **Missing FROM**: `SELECT * account` ❌ → `SELECT * FROM account` ✅
> - **Typo**: `show coloumns` ❌ → `SHOW COLUMNS` ✅
> - **Typo in table name**: `alter table acocunt` ❌ → `ALTER TABLE account` ✅
> - **Empty table**: `CREATE TABLE account;` ❌ → A table must have at least one visible column!
> - **CHECK violation**: Inserting data that violates a `CHECK` constraint will throw `ERROR 3819`.

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=120&section=footer" width="100%" />

</div>
