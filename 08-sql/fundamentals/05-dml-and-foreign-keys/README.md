<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=220&section=header&text=📅%20Day%205%20—%2011%20April%202026&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=DML%20%7C%20Foreign%20Keys%20%7C%20ON%20DELETE%20CASCADE%20%7C%20ON%20DELETE%20SET%20NULL%20%7C%20REPLACE&descSize=16&descAlignY=58&descAlign=50" width="100%" />

<!-- Badges -->
[![MySQL](https://img.shields.io/badge/MySQL-9.6.0-00758f?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![Database](https://img.shields.io/badge/Database-temp-blueviolet?style=for-the-badge&logo=databricks&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Completed%20✅-00c853?style=for-the-badge)](#)

---

### 🧠 Topics Covered Today

| # | Topic | Keyword |
|:-:|:------|:--------|
| 1 | 📝 Data Manipulation | `INSERT`, `UPDATE`, `DELETE` |
| 2 | 🔗 Foreign Keys | `FOREIGN KEY ... REFERENCES` |
| 3 | 💥 Delete Cascading | `ON DELETE CASCADE` |
| 4 | 🚫 Delete Nulifying | `ON DELETE SET NULL` |
| 5 | 🔄 Insert or Update | `REPLACE INTO` |

---

</div>

### ⚡ Quick Reference — Commands & Outputs

#### 🔗 Creating Foreign Keys

```sql
CREATE TABLE Order_details (
    Order_id INT PRIMARY KEY,
    delivery_date DATE,
    cust_id INT,
    FOREIGN KEY (cust_id) REFERENCES customer(id)
);
```

> Trying to delete a parent row (`customer`) when child records (`Order_details`) exist results in:  
> **ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails**

#### 💥 ON DELETE CASCADE

When the parent row is deleted, the corresponding child rows in the related table are also automatically deleted.

```sql
CREATE TABLE Order_details(
    Order_id INT PRIMARY KEY,
    delivery_date DATE,
    cust_id INT,
    FOREIGN KEY(cust_id) REFERENCES customer(id) ON DELETE CASCADE
);
```

#### 🚫 ON DELETE SET NULL

When the parent row is deleted, the foreign key column in the child rows is set to `NULL` (the referenced column must be nullable).

```sql
CREATE TABLE Order_details(
    Order_id INT PRIMARY KEY,
    delivery_date DATE,
    cust_id INT,
    FOREIGN KEY(cust_id) REFERENCES customer(id) ON DELETE SET NULL
);
```

#### 🔄 REPLACE INTO

`REPLACE` works exactly like `INSERT`, except that if an old row in the table has the same value as a new row for a `PRIMARY KEY` or a `UNIQUE` index, the old row is deleted before the new row is inserted.

```sql
-- Acts like INSERT if 'id' 1 does not exist, otherwise updates the existing row by completely replacing it (missing explicit values default to NULL)
REPLACE INTO customer(id,cit) VALUES(1,'rohtak');
```

---

<div align="center">

### 💡 Key Takeaways

| Concept | Syntax |
|:--------|:-------|
| Foreign Key | `FOREIGN KEY(col) REFERENCES parent_table(col)` |
| Cascade Delete | `... ON DELETE CASCADE` |
| Nullify on Delete | `... ON DELETE SET NULL` |
| Replace Row | `REPLACE INTO table (cols) VALUES (vals)` |

---

### ⚠️ Mistakes to Avoid

> [!WARNING]
> - **Syntax Error Typing DESC**: `desc table;` ❌ → `DESC customer;` ✅ (Use the actual table name)
> - **Incomplete statements**: Using `value` instead of `VALUES`, or leaving unclosed strings like `''jalandhar'` ❌
> - **Typo in SELECT**: `slect * from cutomer` ❌ → `SELECT * FROM customer` ✅
> - **Typo in "References"**: `refrences` ❌ → `REFERENCES` ✅
> - **Foreign Key Constraint Failures**: Deleting data from parent tables without handling child tables first generally causes constraint failures unless handled with `CASCADE` or `SET NULL`.
> - `REPLACE INTO` completely replaces the row! Any unspecified columns in the `REPLACE` statement will become `NULL` or their default values if the existing row is replaced.

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=120&section=footer" width="100%" />

</div>
