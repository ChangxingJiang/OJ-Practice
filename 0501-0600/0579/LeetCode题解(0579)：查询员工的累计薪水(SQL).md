# LeetCode题解(0579)：查询员工的累计薪水(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/find-cumulative-salary-of-an-employee/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 336ms (22.34%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
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
```