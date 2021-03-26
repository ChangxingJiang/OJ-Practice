# LeetCode题解(1076)：项目员工II(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/project-employees-ii/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 667ms (22.32%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT project_id
FROM Project
GROUP BY project_id
HAVING COUNT(employee_id) = (SELECT COUNT(employee_id)
                            FROM Project
                            GROUP BY project_id
                            ORDER BY COUNT(employee_id) DESC
                            LIMIT 1);
```

