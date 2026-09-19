show databases;

use movie;
select * from movie;

show tables;
select * from director;
select * from director_name;

show databases;

create database sql_18_may_2026;
show tables;

use sql_18_may_2026;
show tables;

drop database sql_18_may_2026;
show databases;

create database online_database;
use online_database;

create table student(
    name varchar(10) primary key not null,
    Email varchar(100) unique not null,
    course varchar(100),
    created_at timestamp default current_timestamp
);

show tables;

create table admin(
    admin_id int primary key unique not null,
    admin_name  varchar(100)
);

create table teacher(
    teacher_id int primary key unique not null,
    tacher_name varchar(100),
    subject varchar(100)
);

show tables;

alter table teacher
add column teacher_admin_id int unique not null;

select * from teacher;
show create table teacher;

show tables;

select * from admin;
show create table admin;

insert into admin (admin_id , admin_name)
values (1,'Yogender'),
(2,'Yash');

select * from admin;
