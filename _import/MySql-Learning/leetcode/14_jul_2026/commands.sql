select p.product_id, m.first_year ,p.quantity,p.price
from sales p



join(select product_id , min(year) as first_year from sales group by product_id) m
 on m.product_id =p.product_id and m.first_year=p.year;
