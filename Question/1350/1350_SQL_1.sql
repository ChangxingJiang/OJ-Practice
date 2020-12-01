Create table If Not Exists Departments
(
    id int,
    name varchar(30)
);
Create table If Not Exists Students
(
    id int,
    name varchar(30),
    department_id int
);

SELECT id, name
FROM Students
WHERE department_id NOT IN (SELECT id FROM Departments);