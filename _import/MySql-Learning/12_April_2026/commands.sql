create database joins;
use joins;

create table employee(
	id int primary key,
    fname varchar(224) not null,
    lname varchar(224),
    age int not null,
    email_id varchar(224),
    phone_no varchar(15) not null,
    city varchar(50) not null
);
desc employee;
show tables;
select * from employee;

insert into employee(id,fname,lname,age,email_id,phone_no,city)
values
(1,'Aman','Proto',32,'aman@gmail.com','1234567890','delhi'),
(2,'yagya','Proto',31,'yagya@gmail.com','1234567890','mumbai'),
(3,'yash','Proto',33,'yash@gmail.com','1234567890','delhi'),
(4,'Anish','Proto',35,'anish@gmail.com','1234567890','delhi'),
(5,'pk','Proto',30,'pk@gmail.com','1234567890','delhi');

create table project(
	id int primary key,
    emp_id int,
    name varchar(244),
    start_date date,
    client_id int,
    foreign key (emp_id) references employee(id)
);
INSERT INTO project (id, emp_id, name, start_date, client_id)
VALUES
(1, 1, 'A', '2021-04-21', 3),
(2, 2, 'B', '2021-03-12', 1),
(3, 3, 'C', '2021-01-16', 5),
(4, 3, 'D', '2021-04-27', 2),
(5, 5, 'E', '2021-05-01', 4);

create table client(
	id int primary key,
    first_name varchar(224),
    last_name varchar(224),
    age int,
    email_id varchar(224),
    phone_no varchar(10),
    city varchar(20),
    emp_id int,
    foreign key (emp_id) references employee(id)
);
INSERT INTO client (id, first_name, last_name, age, email_id, phone_no, city, emp_id)
VALUES
(1, 'Mac', 'Rogers', 47, 'mac@hotmail.com', '333', 'Kolkata', 3),
(2, 'Max', 'Poilier', 27, 'max@gmail.com', '222', 'Kolkata', 3),
(3, 'Peter', 'Jain', 24, 'peter@abc.com', '111', 'Delhi', 1),
(4, 'Sushant', 'Aggarwal', 23, 'sushant@yahoo.com', '45454', 'Hyderabad', 5),
(5, 'Pratap', 'Singh', 36, 'p.xyz.com', '77767', 'Mumbai', 2);

ALTER TABLE project
ADD FOREIGN KEY (client_id) REFERENCES client(id);
    
-- Inner join 
-- employee id , name ,project id ,project name 
select e.id ,e.fname, e.lname ,p.id, p.name 
from employee as e 
inner join project as p on e.id=p.emp_id;
    
select * from employee as e 
inner join project as p on e.id=p.emp_id;

-- employee id , contact detail who are working from delhi with the clients name working in Kolkata
select * from employee;
select * from client;

select e.id, e.fname, e.phone_no, e.email_id 
from employee as e 
inner join client as c on e.id=c.emp_id 
where (e.city='delhi' and c.city='kolkata');
