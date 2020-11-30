Create table If Not Exists Employee
(
    EmpId int,
    Name varchar(255),
    Supervisor int,
    Salary int
);
Create table If Not Exists Bonus
(
    EmpId int,
    Bonus int
);

SELECT Name, Bonus
FROM Employee
         LEFT JOIN
     Bonus B on Employee.EmpId = B.EmpId
WHERE Bonus IS NULL OR Bonus < 1000;