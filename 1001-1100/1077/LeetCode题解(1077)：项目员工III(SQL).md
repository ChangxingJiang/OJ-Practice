# LeetCode题解(1077)：项目员工III(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/project-employees-iii/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 453ms (33.47%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT P.project_id, P.employee_id
FROM Project AS P
         LEFT JOIN
     Employee AS E on P.employee_id = E.employee_id
WHERE (project_id, experience_years) IN (SELECT project_id, MAX(experience_years) AS MAX
                                         FROM Project
                                                  LEFT JOIN
                                              Employee E on Project.employee_id = E.employee_id
                                         GROUP BY project_id);
```