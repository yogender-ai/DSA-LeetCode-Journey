<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:eeb004&height=220&section=header&text=🧑‍💻%20LeetCode%20—%2021%20May%202026&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Average%20Time%20of%20Process%20per%20Machine%20&%20Employee%20Bonus&descSize=16&descAlignY=58&descAlign=50" width="100%" />

<!-- Badges -->
[![MySQL](https://img.shields.io/badge/MySQL-9.6.0-00758f?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Completed%20✅-eeb004?style=for-the-badge&logo=leetcode&logoColor=white)](#)

---

### 📝 Problem Descriptions

**Q1661. Average Time of Process per Machine**
Write a solution to find the average time each machine takes to complete a process.

**Q577. Employee Bonus**
Write a solution to report the name and bonus amount of each employee who has a bonus less than 1000 or did not get any bonus.

---

</div>

### 💡 Solutions

#### 1661. Average Time of Process per Machine
```sql
# Write your MySQL query statement below
SELECT machine_id, 
       ROUND(AVG(CASE WHEN activity_type = 'end' THEN timestamp END) - 
             AVG(CASE WHEN activity_type = 'start' THEN timestamp END), 3) AS processing_time 
FROM activity 
GROUP BY machine_id;
```

#### 577. Employee Bonus
```sql
# Write your MySQL query statement below
SELECT e.name, b.bonus 
FROM employee AS e 
LEFT JOIN bonus AS b ON e.empId = b.empId 
WHERE bonus < 1000 OR bonus IS NULL;
```

---

<div align="center">

### 🧠 Key Concepts

| Concept | Explanation |
|:--------|:------------|
| `Conditional Aggregation` | Using `CASE WHEN` inside aggregate functions like `AVG()` to perform calculations based on conditions. |
| `LEFT JOIN` | Joining tables to include all rows from the left table, even if there are no matches in the right table (useful for finding missing bonuses). |

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:eeb004&height=120&section=footer" width="100%" />

</div>
