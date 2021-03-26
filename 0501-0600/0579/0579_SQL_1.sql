Create table If Not Exists Employee
(
    Id int,
    Month int,
    Salary int
);

# Step 1
# 查询每个员工的最大月份
SELECT Id, MAX(Month)
FROM Employee
GROUP BY Id;

# Step 2
# 查询每个员工的非最大月份
SELECT Id, Month, Salary
FROM Employee
WHERE (Id, Month) NOT IN (SELECT Id, MAX(Month)
                          FROM Employee
                          GROUP BY Id);

# Step 3
# 查询每个员工的最近三个月的累计工资
SELECT E1.Id,
       E1.Month,
       (IFNULL(E1.Salary, 0) + IFNULL(E2.Salary, 0) + IFNULL(E3.Salary, 0)) AS Salary
FROM Employee AS E1
         LEFT JOIN
     Employee AS E2 ON (E2.Id = E1.Id AND E2.Month = E1.Month - 1)
         LEFT JOIN
     Employee AS E3 ON (E3.Id = E1.Id AND E3.Month = E1.Month - 2)
ORDER BY E1.Id, E1.Month DESC;

# Step 4
SELECT E1.Id AS Id,
       E1.Month AS Month,
       (IFNULL(E1.Salary, 0) + IFNULL(E2.Salary, 0) + IFNULL(E3.Salary, 0)) AS Salary
FROM Employee AS E1
         LEFT JOIN
     Employee AS E2 ON (E2.Id = E1.Id AND E2.Month = E1.Month - 1)
         LEFT JOIN
     Employee AS E3 ON (E3.Id = E1.Id AND E3.Month = E1.Month - 2)
WHERE (E1.Id, E1.Month) NOT IN (SELECT Id, MAX(Month)
                                FROM Employee
                                GROUP BY Id)
ORDER BY E1.Id, E1.Month DESC;