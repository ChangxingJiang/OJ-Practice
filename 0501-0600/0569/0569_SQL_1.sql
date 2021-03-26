Create table If Not Exists Employee
(
    Id int,
    Company varchar(255),
    Salary int
);



SELECT Id, Company, Salary
FROM Employee
WHERE Id in (
    SELECT E1.Id
    FROM Employee AS E1
             JOIN
         Employee AS E2 ON E1.Company = E2.Company
    GROUP BY E1.Id
    HAVING SUM(IF(E1.Salary >= E2.Salary, 1, 0)) >= COUNT(*) / 2
       AND SUM(IF(E1.Salary <= E2.Salary, 1, 0)) >= COUNT(*) / 2
)
GROUP BY Company, Salary
ORDER BY Company

