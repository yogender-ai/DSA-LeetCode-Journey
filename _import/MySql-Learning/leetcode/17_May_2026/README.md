<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:eeb004&height=220&section=header&text=🧑‍💻%20LeetCode%20—%2017%20May%202026&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Rising%20Temperature&descSize=16&descAlignY=58&descAlign=50" width="100%" />

<!-- Badges -->
[![MySQL](https://img.shields.io/badge/MySQL-9.6.0-00758f?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Completed%20✅-eeb004?style=for-the-badge&logo=leetcode&logoColor=white)](#)

---

### 📝 Problem Description

**Q197. Rising Temperature**
Write a solution to find all dates' `id` with higher temperatures compared to its previous dates (yesterday). Return the result table in any order.

---

</div>

### 💡 Solution

#### 197. Rising Temperature
```sql
# Write your MySQL query statement below
SELECT today.id 
FROM Weather today 
JOIN Weather yes 
  ON yes.recordDate = DATE_SUB(today.recordDate, INTERVAL 1 DAY) 
WHERE yes.temperature < today.temperature;
```

---

<div align="center">

### 🧠 Key Concepts

| Concept | Explanation |
|:--------|:------------|
| `Self JOIN` | Joining a table with itself to compare rows within the same table. |
| `DATE_SUB()` | Subtracts a time value (interval) from a date. Useful for comparing consecutive days. |

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:eeb004&height=120&section=footer" width="100%" />

</div>
