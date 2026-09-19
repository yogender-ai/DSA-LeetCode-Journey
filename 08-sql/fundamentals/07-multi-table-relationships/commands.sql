create database movie;
use movie;

select database();

create table movie(
    movie_id int primary key,
    movie_name varchar(100)
);

create table director(
    director_id int primary key,
    movie_id int,
    foreign key (movie_id) references movie(movie_id)
);

create table director_name(
    director_name_id int primary key,
    director_name varchar(100),
    director_id int,
    foreign key (director_id) references director(director_id)
);

show tables;
desc movie;
desc director;

insert into movie(movie_id, movie_name)
values 
(1, 'Inception'),
(2, 'INtersteallar');

select * from movie;

insert into director(director_id, movie_id)
values
(1101, 1),
(1102, 2);

show tables;
desc director_name;

insert into director_name(director_name_id, director_name, director_id)
values
(1231, 'Christopher Nolan', 1101),
(1232, 'Yogender', 1102);

select * from director;
select * from director_name;
select * from movie;
