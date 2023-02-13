#Creating Schema
CREATE SCHEMA `Sample_Schema`;
USE `Sample_Schema`;

#Question - 1

#Creating Table 
create table if not exists employees( 
  emp_id integer(4) not null unique, 
  emp_name varchar(30), 
  Gender varchar(10), 
  Department varchar(30), 
  check(
    Gender in ("Male", "Female")
  )
);

#Inserting given data
Insert into employees values 
  (1, 'X', 'Female', 'Finance'), 
  (2, 'Y', 'Male', 'IT'), 
  (3, 'Z', 'Male', 'HR'), 
  (4, 'W', 'Female', 'IT');

#Query to find the number of male and female employees in each department
SELECT IFNULL(Department, 'Not Assigned') as Department, 
COUNT(
	CASE WHEN UPPER(Gender)= 'MALE' THEN 1 END
) AS 'Num of Male', 
COUNT(
    CASE WHEN UPPER(Gender)= 'FEMALE' THEN 1 END) AS 'Num of Female' 
FROM employees 
GROUP BY Department 
order by Department;


#Question - 2

#Creating Table 
create table if not exists employeesalaries (
  emp_name varchar(30) not null, 
  Jan Float(10, 2) Not null default 0, 
  Feb Float(10, 2) Not null default 0, 
  March Float(10, 2) Not null default 0, 
  check(
    Jan >= 0 and Feb >= 0 and March >= 0
  )
);

#Inserting Values
Insert into employeesalaries values 
  ('X', 5200, 9093, 3832), 
  ('Y', 9023, 8942, 4000), 
  ('Z', 9834, 8197, 9903), 
  ('W', 3244, 4321, 0293);

#Query to find the max amount from the rows with month name
select emp_name as Name, 
value, case when id = 1 then 'Jan' when id = 2 then 'Feb' when id = 3 then 'Mar' end as Month 
from (
    select emp_name, greatest(Jan, Feb, March) as value, 
      field( greatest(Jan, Feb, March), 
        Jan, Feb, March
      ) as id 
    from employeesalaries
  ) emps;
  
  
#Question - 3

#Creating Table 
create table if not exists test (
  candidate_id integer(4) not null unique, 
  marks float(10, 2) default 0
);

#Inserting Values
Insert into test values 
  (1, 98), 
  (2, 78), 
  (3, 87), 
  (4, 98), 
  (5, 78);
  
#Query to order marks obtained by candidates in a particular test
SELECT Marks, dense_rank() OVER (
    order by 
      marks desc
) as 'Rank', 
GROUP_CONCAT(Candidate_id) as Candidate_id FROM test 
GROUP BY marks;
 
#Question - 4
#Creation of Table 
create table if not exists mailids (
  candidate_id integer(4) not null unique, 
  mail varchar(30) not null
);

#Inserting given data
Insert into mailids values 
  (45, 'abc@gmail.com'), 
  (23, 'def@yahoo.com'), 
  (34, 'abc@gmail.com'), 
  (21, 'bcf@gmail.com'), 
  (94, 'def@yahoo.com');

#Query to keep the value that has smallest id and delete all the other rows having same value.
DELETE FROM mailids 
WHERE candidate_id in (
    Select tempcandidate_id from (
        select Distinct m1.candidate_id as tempcandidate_id 
        from mailids m1
		inner join mailids m2
        where m1.mail = m2.mail and m1.candidate_id > m2.candidate_id
      ) as c
); 

SELECT * FROM Sample_Schema.mailids order by candidate_id DESC; 

