<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:eeb004&height=220&section=header&text=🧑‍💻%20LeetCode%20—%2022%20May%202026&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Multiple%20SQL%20Problems&descSize=16&descAlignY=58&descAlign=50" width="100%" />

<!-- Badges -->
[![MySQL](https://img.shields.io/badge/MySQL-9.6.0-00758f?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Completed%20✅-eeb004?style=for-the-badge&logo=leetcode&logoColor=white)](#)

---

### 📝 Problem Descriptions

**Q1934. Confirmation Rate**
Write a solution to find the confirmation rate of each user.

**Q570. Managers with at Least 5 Direct Reports**
Write a solution to find managers with at least five direct reports.

**Q620. Not Boring Movies**
Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".

**Q1251. Average Selling Price**
Write a solution to find the average selling price for each product.

**Q1075. Project Employees I**
Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.

**Q1633. Percentage of Users Attended a Contest**
Write a solution to find the percentage of the users registered in each contest rounded to two decimals.

**Q1211. Queries Quality and Percentage**
Write a solution to find each query_name, the quality and poor_query_percentage.

**Q1193. Monthly Transactions I**
Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

---

</div>

### 💡 Solutions

#### 1934. Confirmation Rate
```sql
SELECT s.user_id, 
       ROUND(IFNULL((COUNT(CASE WHEN c.action = 'confirmed' THEN action END)) / (COUNT(action)), 0), 2) AS confirmation_rate 
FROM signups s 
LEFT JOIN confirmations c ON s.user_id = c.user_id 
GROUP BY s.user_id 
ORDER BY confirmation_rate;
```

#### 570. Managers with at Least 5 Direct Reports
```sql
SELECT e.name 
FROM employee e 
JOIN employee em ON e.id = em.managerId 
GROUP BY e.id, e.name
HAVING COUNT(e.id) >= 5;
```

#### 620. Not Boring Movies
```sql
SELECT id, movie, description, rating 
FROM cinema 
WHERE id % 2 != 0 AND description != 'boring'
ORDER BY rating DESC;
```

#### 1251. Average Selling Price
```sql
SELECT p.product_id, 
       IFNULL(ROUND(SUM(u.units * p.price) / SUM(units), 2), 0) AS average_price 
FROM prices p 
LEFT JOIN UnitsSold u ON p.product_id = u.product_id 
                      AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;
```

#### 1075. Project Employees I
```sql
SELECT p.project_id, 
       ROUND(SUM(e.experience_years) / COUNT(p.employee_id), 2) AS average_years
FROM project p 
JOIN employee e ON p.employee_id = e.employee_id 
GROUP BY p.project_id;
```

#### 1633. Percentage of Users Attended a Contest
```sql
SELECT r.contest_id, 
       ROUND(COUNT(u.user_id) / (SELECT COUNT(user_id) FROM users) * 100, 2) AS percentage 
FROM users u 
RIGHT JOIN register r ON u.user_id = r.user_id
GROUP BY r.contest_id 
ORDER BY percentage DESC, r.contest_id ASC;
```

#### 1211. Queries Quality and Percentage
```sql
SELECT query_name, 
       ROUND(SUM(rating / position) / COUNT(position), 2) AS quality, 
       ROUND(COUNT(CASE WHEN rating < 3 THEN 1 ELSE NULL END) / COUNT(rating) * 100, 2) AS poor_query_percentage 
FROM queries 
GROUP BY query_name;
```

#### 1193. Monthly Transactions I
```sql
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, 
       country, 
       COUNT(amount) AS trans_count, 
       COUNT(CASE WHEN state = 'approved' THEN amount END) AS approved_count, 
       SUM(amount) AS trans_total_amount, 
       IFNULL(SUM(CASE WHEN state = 'approved' THEN amount END), 0) AS approved_total_amount 
FROM transactions
GROUP BY DATE_FORMAT(trans_date, '%Y-%m'), country;
```

---

<div align="center">

### 🧠 Key Concepts

| Concept | Explanation |
|:--------|:------------|
| `Conditional Aggregation` | Combining `COUNT`/`SUM` with `CASE WHEN` to aggregate based on specific conditions. |
| `DATE_FORMAT()` | Used to format dates, especially extracting Year-Month for grouping. |
| `HAVING` clause | Filtering grouped data based on aggregate functions (e.g. `COUNT(id) >= 5`). |

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:eeb004&height=120&section=footer" width="100%" />

</div>
