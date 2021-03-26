# LeetCode题解(1350)：院系无效的学生(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/students-with-invalid-departments/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 601ms (50.58%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```MYSQL
SELECT id, name
FROM Students
WHERE department_id NOT IN (SELECT id FROM Departments);
```