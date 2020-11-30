Create table If Not Exists Employee
(
    Id int,
    Name varchar(255),
    Salary int,
    DepartmentId int
);
Create table If Not Exists Department
(
    Id int,
    Name varchar(255)
);

SELECT Department.name AS Department,
       e1.name AS Employee,
       e1.salary AS Salary
FROM Employee AS e1
         JOIN
     Department ON e1.departmentid = Department.Id
WHERE 3 > (
    SELECT COUNT(DISTINCT e2.salary)
    FROM employee AS e2
    WHERE e2.salary > e1.salary
      AND e1.DepartmentId = e2.DepartmentId
);