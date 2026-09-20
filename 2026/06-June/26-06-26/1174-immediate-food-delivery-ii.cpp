/*
 * LeetCode 1174 · Immediate Food Delivery II · Medium
 * https://leetcode.com/problems/immediate-food-delivery-ii/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

// ==========================================================
//  CodeShelf — LeetCode Solution
// ==========================================================
//  Problem:    Immediate Food Delivery II
//  URL:        https://leetcode.com/problems/immediate-food-delivery-ii/submissions/2014966104/?envType=study-plan-v2&envId=top-sql-50
//  Difficulty: Hard
//  Tags:       Database
//  Approach:  Table: Delivery
//             
//             +-----------------------------+---------+
//             | Column Name                 | Type    |
//             +-----------------------------+---------+
//             | delivery_id                 | int     |
//             | customer_id                 | int     |
//             | order_date                  | date    |
//             | customer_pref_delivery_date | date    |
//             +-----------------------------+---------+
//             delivery_id is the column of unique values of this table.
//             The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).
//             
//             
//             
//             
//             If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.
//             
//             The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.
//             
//             Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.
//             
//             The result format is in the following example.
//             
//             
//             Example 1:
//             
//             Input:
//             Delivery table:
//             +-------------+-------------+------------+-----------------------------+
//             | delivery_id | customer_id | order_date | customer_pref_delivery_date |
//             +-------------+-------------+------------+-----------------------------+
//             | 1           | 1           | 2019-08-01 | 2019-08-02                  |
//             | 2           | 2           | 2019-08-02 | 2019-08-02                  |
//             | 3           | 1           | 2019-08-11 | 2019-08-12                  |
//             | 4           | 3           | 2019-08-24 | 2019-08-24
// ==========================================================
    ) AS immediate_percentage
 from (select d.*, row_number() over (partition by customer_id 
 order by order_date)as r 
 from delivery d) x
  where r=1;
                ELSE 0 
            END) * 100.0 / COUNT(*),
        2
                WHEN order_date = customer_pref_delivery_date 
                THEN 1
