Create table If Not Exists Employee
(
    Id int,
    Name varchar(255),
    Department varchar(255),
    ManagerId int
);

SELECT Name
FROM Employee
WHERE Id IN (
    SELECT ManagerId
    FROM Employee
    GROUP BY ManagerId
    HAVING COUNT(`Name`) >= 5);
