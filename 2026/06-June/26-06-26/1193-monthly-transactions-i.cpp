/*
 * LeetCode 1193 · Monthly Transactions I · Medium
 * https://leetcode.com/problems/monthly-transactions-i/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

// ==========================================================
//  CodeShelf — LeetCode Solution
// ==========================================================
//  Problem:    Monthly Transactions I
//  URL:        https://leetcode.com/problems/monthly-transactions-i/?envType=study-plan-v2&envId=top-sql-50
//  Difficulty: Hard
//  Tags:       Database
//  Approach:  Table: Transactions
//             
//             +---------------+---------+
//             | Column Name   | Type    |
//             +---------------+---------+
//             | id            | int     |
//             | country       | varchar |
//             | state         | enum    |
//             | amount        | int     |
//             | trans_date    | date    |
//             +---------------+---------+
//             id is the primary key of this table.
//             The table has information about incoming transactions.
//             The state column is an enum of type ["approved", "declined"].
//             
//             
//             
//             
//             Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.
//             
//             Return the result table in any order.
//             
//             The query result format is in the following example.
//             
//             
//             Example 1:
//             
//             Input:
//             Transactions table:
//             +------+---------+----------+--------+------------+
//             | id   | country | state    | amount | trans_date |
//             +------+---------+----------+--------+------------+
//             | 121  | US      | approved | 1000   | 2018-12-18 |
//             | 122  | US      | declined | 2000   | 2018-12-19 |
//             | 123  | US      | approved | 2000   | 2019-01-01 |
//             | 124  | DE      | approved | 2000   | 2019-01-07 |
//             +------+---------+----------+--------+------------+
//             Output:
//             +----------+---------+-------------+----------------+--------------------+-----------------------+
//             | month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
//             +----------+---------+-------------+----------------+--------------------+-----------------------+
//             | 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
//             | 2019-01  | US      | 1           | 1
// ==========================================================
select date_format(trans_date,"%Y-%m") as month , 
country , 
count(amount) as trans_count , 
count(case when state= "approved"  then amount end) as 
approved_count , 
sum(amount) as trans_total_amount , 
ifnull(sum(case when state="approved" then amount end),0) as 
approved_total_amount 
from transactions
 group by date_format(trans_date,"%Y-%m"),country;
