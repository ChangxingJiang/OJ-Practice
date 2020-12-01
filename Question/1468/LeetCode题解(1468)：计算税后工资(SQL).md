# LeetCode题解(1468)：计算税后工资(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/calculate-salaries/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 461ms (84.69%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT company_id,
       employee_id,
       employee_name,
       ROUND(salary * tax) AS salary
FROM Salaries
         LEFT JOIN
     (SELECT company_id,
             CASE
                 WHEN MAX(salary) < 1000 THEN 1
                 WHEN MAX(salary) BETWEEN 1000 AND 10000 THEN 1 - 0.24
                 ELSE 1 - 0.49
                 END AS tax
      FROM Salaries
      GROUP BY company_id) AS T USING (company_id);
```