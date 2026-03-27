# 📅 Day 1 — 27 March 2026
### *MySQL Fundamentals & Filtering*

---

### 🧠 Topics Covered
- **Exploration**: `SHOW DATABASES`, `SHOW TABLES`
- **Filtering**: `WHERE`, `BETWEEN`, `IN`, `LIKE`
- **Sorting**: `ORDER BY` (ASC/DESC)
- **Functions**: `NOW()`, Math Operations

---

### ⚡ Quick Reference

#### 1. Basic Data Retrieval
```sql
SELECT * FROM worker;
SELECT salary, last_name FROM worker;
```

#### 2. Filtering with WHERE
```sql
-- Range & Multi-value
SELECT * FROM worker WHERE salary BETWEEN 100000 AND 500000;
SELECT * FROM worker WHERE department IN ('HR', 'Admin');

-- Pattern Matching
SELECT * FROM worker WHERE first_name LIKE '%vi%';
```

#### 3. Sorting Results
```sql
SELECT * FROM worker ORDER BY salary DESC;
```

---

### 💡 Key Takeaways
- Use `IN` instead of multiple `OR` for cleaner code.
- `%` is the wildcard for 0 or more characters in `LIKE`.
- MySQL string comparisons are case-insensitive by default.

---
[⬅️ Back to Master Journal](../README.md)
