# LeetCode题解(1378)：使用唯一标识码替换员工ID(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/replace-employee-id-with-the-unique-identifier/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 665ms (63.40%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT EmployeeUNI.unique_id,
       Employees.name
FROM Employees
         LEFT JOIN
    EmployeeUNI ON Employees.id = EmployeeUNI.id;
```