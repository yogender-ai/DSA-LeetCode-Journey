<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=220&section=header&text=📅%20Day%208%20—%2015%20May%202026&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Foreign%20Keys%20%7C%20Relationships%20%7C%20Multiple%20Tables&descSize=16&descAlignY=58&descAlign=50" width="100%" />

<!-- Badges -->
[![MySQL](https://img.shields.io/badge/MySQL-9.6.0-00758f?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![Database](https://img.shields.io/badge/Database-movie-blueviolet?style=for-the-badge&logo=databricks&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Completed%20✅-00c853?style=for-the-badge)](#)

---

### 🧠 Topics Covered Today

| # | Topic | Keyword |
|:-:|:------|:--------|
| 1 | 🔗 Foreign Keys | `FOREIGN KEY` |
| 2 | 📊 Multiple Tables | `CREATE TABLE` |
| 3 | 💾 Data Insertion | `INSERT INTO` |

---

</div>

### ⚡ Quick Reference — Commands & Outputs

#### 🔗 SQL Foreign Key Example

The `FOREIGN KEY` constraint is used to prevent actions that would destroy links between tables. We created a `movie` database with `movie`, `director`, and `director_name` tables to practice relational data structure.

```sql
-- create tables with primary and foreign keys
create table movie(
    movie_id int primary key,
    movie_name varchar(100)
);

create table director(
    director_id int primary key,
    movie_id int,
    foreign key (movie_id) references movie(movie_id)
);

create table director_name(
    director_name_id int primary key,
    director_name varchar(100),
    director_id int,
    foreign key (director_id) references director(director_id)
);
```

---

<div align="center">

### 💡 Key Takeaways

| Concept | Syntax |
|:--------|:-------|
| Foreign Key | `FOREIGN KEY (col_name) REFERENCES other_table(col_name)` |
| Structure | First create the table being referenced, then the one that references it. |

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:0ea5e9&height=120&section=footer" width="100%" />

</div>
