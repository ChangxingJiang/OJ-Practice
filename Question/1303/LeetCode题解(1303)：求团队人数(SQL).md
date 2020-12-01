# LeetCode题解(1303)：求团队人数(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-team-size/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 194ms (92.32%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT E.employee_id,
       T.team_size
FROM Employee AS E
         LEFT JOIN
     (SELECT team_id,
             COUNT(employee_id) AS team_size
      FROM Employee
      GROUP BY team_id) AS T ON E.team_id = T.team_id;
```