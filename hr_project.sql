
CREATE DATABASE hr_project;
USE hr_project;

CREATE TABLE EMP
(
emp_id INT primary key,
ename varchar(50),
dept varchar(50),
gender varchar(10),
age int,
salary int,
experience int,
city varchar(30),
join_date date,
performance_rating int
);

INSERT INTO EMP VALUES
(101,'Rahul','IT','Male',26,50000,2,'Hyderabad','2022-01-15',4),

(102,'Priya','HR','Female',29,45000,4,'Bangalore','2021-05-10',5),

(103,'Ajay','Finance','Male',32,60000,7,'Chennai','2018-08-20',3),

(104,'Sneha','IT','Female',25,55000,3,'Hyderabad','2022-06-18',5),

(105,'Kiran','Sales','Male',30,40000,5,'Pune','2020-11-11',2),

(106,'Meena','Finance','Female',28,62000,6,'Delhi','2019-09-09',4),

(107,'Arjun','IT','Male',27,52000,3,'Hyderabad','2021-12-01',5),

(108,'Divya','HR','Female',31,47000,6,'Mumbai','2019-07-17',4),

(109,'Ravi','Sales','Male',35,39000,9,'Bangalore','2016-02-10',3),

(110,'Pooja','IT','Female',24,51000,2,'Hyderabad','2023-03-01',5);

SELECT * FROM EMP;

SHOW TABLES;
DESCRIBE EMP;

