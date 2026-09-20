<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=220&section=header&text=📅%20Day%2011%20—%2018%20May%202026&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=CREATE%20DATABASE%20%7C%20Table%20Constraints%20%7C%20ALTER%20TABLE&descSize=16&descAlignY=58&descAlign=50" width="100%" />

<!-- Badges -->
[![MySQL](https://img.shields.io/badge/MySQL-9.6.0-00758f?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![Database](https://img.shields.io/badge/Database-online__database-blueviolet?style=for-the-badge&logo=databricks&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Completed%20✅-00c853?style=for-the-badge)](#)

---

### 🧠 Topics Covered Today

| # | Topic | Keyword |
|:-:|:------|:--------|
| 1 | 🗄️ Database Management | `CREATE / DROP DATABASE` |
| 2 | 🏗️ Table Creation & Constraints | `CREATE TABLE`, `PRIMARY KEY`, `UNIQUE` |
| 3 | 🔄 Modifying Schema | `ALTER TABLE` |
| 4 | 📝 Data Insertion | `INSERT INTO` |

---

</div>

### ⚡ Quick Reference — Commands & Outputs

#### 🗄️ Managing Databases

We practiced creating and dropping databases, as well as checking the available ones.

```sql
create database sql_18_may_2026;

use sql_18_may_2026;

drop database sql_18_may_2026;

create database online_database;
use online_database;
```

#### 🏗️ Creating Tables with Constraints

We created tables for `student`, `admin`, and `teacher` inside `online_database`, utilizing constraints like `PRIMARY KEY`, `UNIQUE`, `NOT NULL`, and `DEFAULT CURRENT_TIMESTAMP`.

```sql
create table student(
    name varchar(10) primary key not null,
    Email varchar(100) unique not null,
    course varchar(100),
    created_at timestamp default current_timestamp
);

create table admin(
    admin_id int primary key unique not null,
    admin_name  varchar(100)
);

create table teacher(
    teacher_id int primary key unique not null,
    tacher_name varchar(100),
    subject varchar(100)
);
```

#### 🔄 Modifying Schema

We used `ALTER TABLE` to add a new column to the `teacher` table with specific constraints.

```sql
alter table teacher
add column teacher_admin_id int unique not null;
```

#### 📝 Data Insertion

We inserted records into the `admin` table.

```sql
insert into admin (admin_id , admin_name)
values (1,'Yogender'),
(2,'Yash');
```

**Output:**
```text
+----------+------------+
| admin_id | admin_name |
+----------+------------+
|        1 | Yogender   |
|        2 | Yash       |
+----------+------------+
```

---

<div align="center">

### 💡 Key Takeaways

| Concept | Syntax |
|:--------|:-------|
| Database Creation | `CREATE DATABASE db_name;` |
| Table Creation with Constraints | `CREATE TABLE table_name(col1 INT PRIMARY KEY NOT NULL, col2 VARCHAR(50) UNIQUE);` |
| Add Column with Constraints | `ALTER TABLE table_name ADD COLUMN new_col INT UNIQUE NOT NULL;` |
| Default Timestamps | `created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP` |

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=120&section=footer" width="100%" />

</div>
