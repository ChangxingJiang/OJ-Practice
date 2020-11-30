# LeetCode题解(0569)：员工薪水中位数(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/median-employee-salary/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 570ms (21.51%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
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
```