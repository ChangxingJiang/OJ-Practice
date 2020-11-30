# LeetCode题解(0185)：部门工资前三高的所有员工(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/department-top-three-salaries/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 957ms (34.12%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

```mysql
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
```

解法一：

```mysql
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
```