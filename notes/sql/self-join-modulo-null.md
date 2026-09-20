<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:eeb004&height=220&section=header&text=🧑‍💻%20LeetCode%20—%2018%20April%202026&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Managers%20%7C%20Movies%20%7C%20Referees&descSize=16&descAlignY=58&descAlign=50" width="100%" />

<!-- Badges -->
[![MySQL](https://img.shields.io/badge/MySQL-9.6.0-00758f?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Completed%20✅-eeb004?style=for-the-badge&logo=leetcode&logoColor=white)](#)

---

### 📝 Problem Descriptions

**Q2. Employees Earning More Than Their Managers**
Write a solution to find the employees who earn more than their managers.

**Q3. Not Boring Movies**
Write a solution to report the movies with an odd-numbered ID and a description that is not "boring". Return the result table ordered by rating in descending order.

**Q4. Find Customer Referee**
Write a solution to report the names of the customer that are not referred by the customer with `id = 2`.

---

</div>

### 💡 Solutions

#### 1. Employees Earning More Than Their Managers
```sql
# Write your MySQL query statement below
SELECT e.name AS Employee 
FROM Employee AS e 
JOIN Employee m ON e.managerId = m.id 
WHERE e.salary > m.salary;
```

#### 2. Not Boring Movies
```sql
# Write your MySQL query statement below
SELECT * 
FROM Cinema 
WHERE id % 2 != 0 AND description != 'boring' 
ORDER BY rating DESC;
```

#### 3. Find Customer Referee
```sql
# Write your MySQL query statement below
SELECT name 
FROM Customer 
WHERE referee_id != 2 OR referee_id IS NULL;
```

---

<div align="center">

### 🧠 Key Concepts

| Concept | Explanation |
|:--------|:------------|
| `Self JOIN` | Joining a table with itself to compare rows within the same table (e.g., matching employees to managers). |
| `Modulo Operator (%)` | Used to find remainders; `id % 2 != 0` identifies odd-numbered IDs. |
| `NULL Handling` | Using `IS NULL` or `OR` conditions to ensure records with missing values are correctly filtered or included. |

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:eeb004&height=120&section=footer" width="100%" />

</div>
