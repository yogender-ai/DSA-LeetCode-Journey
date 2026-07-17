select distinct num as ConsecutiveNums from 
(select id,num , lag(num,1) over (order by id) as prev1,
lag (num,2) over (order by id) as prev2 
from Logs) t 
where t.num=t.prev1 and t.prev1=t.prev2;
select x,y,z,
case
when (x+y>z&&y+z>x&&z+x>y) then 'Yes'
else 'No'
end as triangle
from Triangle; 

-----------------------------------------------

q3:- 
select employee_id, department_id from employee where primary_flag='Y'
union
select employee_id, department_id from employee group by employee_id having count(employee_id)=1; 
