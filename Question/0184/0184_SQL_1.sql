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
       Employee.name AS Employee,
       salary AS Salary
FROM Employee
         JOIN
     Department ON Employee.departmentid = Department.Id
WHERE (Employee.departmentid, salary) IN
      (
          SELECT departmentid, max(salary)
          FROM employee
          GROUP BY departmentid
      );