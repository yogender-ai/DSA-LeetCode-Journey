<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:eeb004&height=220&section=header&text=🧑‍💻%20LeetCode%20—%2012%20April%202026&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Combine%20Two%20Tables%20%7C%20LEFT%20JOIN&descSize=16&descAlignY=58&descAlign=50" width="100%" />

<!-- Badges -->
[![MySQL](https://img.shields.io/badge/MySQL-9.6.0-00758f?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Completed%20✅-eeb004?style=for-the-badge&logo=leetcode&logoColor=white)](#)

---

### 📝 Problem Description

**Q1. Combine Two Tables**

Write a solution to report the first name, last name, city, and state of each person in the `Person` table. If the address of a `personId` is not present in the `Address` table, report `null` instead.

Return the result table in **any order**.

---

</div>

### 💡 Solution

```sql
# Write your MySQL query statement below
SELECT p.firstName, p.lastName, a.city, a.state 
FROM Person AS p 
LEFT JOIN Address AS a ON p.personId = a.personId;
```

---

<div align="center">

### 🧠 Key Concepts

| Concept | Explanation |
|:--------|:------------|
| `LEFT JOIN` | Keeps **all** records from the left table (`Person`), even if there are no matches in the right table (`Address`). Any missing values from the right table are represented as `NULL`. |

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:eeb004&height=120&section=footer" width="100%" />

</div>
