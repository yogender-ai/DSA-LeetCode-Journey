-- LeetCode 1789 · Primary Department for Each Employee · Easy
-- https://leetcode.com/problems/primary-department-for-each-employee/
--
-- Pattern : SQL
-- Solved  : 17 Jul 2026
-- Time    : O(n)
-- Space   : O(1)

select employee_id, department_id from employee where primary_flag='Y'
union
select employee_id, department_id from employee group by employee_id having count(employee_id)=1;
