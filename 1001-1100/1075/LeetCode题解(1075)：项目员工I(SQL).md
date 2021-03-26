# LeetCode题解(1075)：项目员工I(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/project-employees-i/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 666ms (20.50%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT project_id, ROUND(AVG(experience_years),2) AS average_years
FROM Project
         LEFT JOIN
     Employee E on Project.employee_id = E.employee_id
GROUP BY project_id;
```

