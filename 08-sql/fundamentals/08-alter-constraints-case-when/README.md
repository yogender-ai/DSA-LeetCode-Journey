<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=220&section=header&text=📅%20Day%209%20—%2017%20May%202026&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=ALTER%20TABLE%20%7C%20CASE%20WHEN%20Updates%20%7C%20Complex%20JOINs&descSize=16&descAlignY=58&descAlign=50" width="100%" />

<!-- Badges -->
[![MySQL](https://img.shields.io/badge/MySQL-9.6.0-00758f?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![Database](https://img.shields.io/badge/Database-movie-blueviolet?style=for-the-badge&logo=databricks&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Completed%20✅-00c853?style=for-the-badge)](#)

---

### 🧠 Topics Covered Today

| # | Topic | Keyword |
|:-:|:------|:--------|
| 1 | 🔄 Modifying Schema | `ALTER TABLE` |
| 2 | 🔗 Modifying Constraints | `DROP/ADD FOREIGN KEY` |
| 3 | 🔀 Conditional Updates | `CASE WHEN` |
| 4 | 🤝 Complex Joins | `JOIN` |

---

</div>

### ⚡ Quick Reference — Commands & Outputs

#### 🔄 Dropping & Adding Foreign Keys

To reorganize the database schema, we dropped existing foreign key constraints and applied new ones linking tables differently.

```sql
-- Dropping a foreign key constraint
alter table director_name
drop foreign key director_name_ibfk_1;

-- Adding a new foreign key constraint with a custom name
alter table director_name
add constraint fk
foreign key (director_id) references movie(movie_id);
```

#### 🛠️ Modifying Columns

We modified the `director` table by dropping the old `movie_id` column and adding a new `name_id` column to reference `director_name`.

```sql
alter table director
drop column movie_id;

alter table director
add column name_id int not null;
```

#### 🔀 Updating Rows using CASE WHEN

Instead of running multiple `UPDATE` queries, we used `CASE WHEN` to update multiple records conditionally in a single query.

```sql
update director_name
set director_id = CASE
    when director_name_id = 1231 then 1
    when director_name_id = 1232 then 2
end
where director_name_id in (1231, 1232);

update director
set name_id = CASE
    when director_id = 1101 then 1231
    when director_id = 1102 then 1232
end
where director_id in (1101, 1102);
```

#### 🤝 Complex Joins

Finally, we executed a 3-table `JOIN` query to fetch data from `movie`, `director_name`, and `director` using our newly mapped foreign keys.

```sql
select m.movie_name, d.director_name, n.director_id 
from movie as m 
join director_name as d on d.director_id = m.movie_id 
join director as n on n.name_id = d.director_name_id;
```

**Output:**
```text
+---------------+-------------------+-------------+
| movie_name    | director_name     | director_id |
+---------------+-------------------+-------------+
| Inception     | Christopher Nolan |        1101 |
| INtersteallar | Yogender          |        1102 |
+---------------+-------------------+-------------+
```

---

<div align="center">

### 💡 Key Takeaways

| Concept | Syntax |
|:--------|:-------|
| Drop Constraint | `ALTER TABLE table_name DROP FOREIGN KEY fk_name;` |
| Add Constraint | `ALTER TABLE table_name ADD CONSTRAINT fk_name FOREIGN KEY (col) REFERENCES other_table(col);` |
| Conditional Update | `UPDATE table SET col = CASE WHEN condition THEN val END WHERE condition;` |

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=120&section=footer" width="100%" />

</div>
