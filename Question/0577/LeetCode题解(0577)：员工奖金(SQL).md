# LeetCode题解(0577)：员工奖金(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/employee-bonus/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 206ms (85.86%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT Name, Bonus
FROM Employee
         LEFT JOIN
     Bonus B on Employee.EmpId = B.EmpId
WHERE Bonus IS NULL OR Bonus < 1000;
```