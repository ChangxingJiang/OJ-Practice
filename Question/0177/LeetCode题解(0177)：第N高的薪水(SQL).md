# LeetCode题解(0177)：第N高的薪水(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/nth-highest-salary/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 256ms (73.95%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N:=N-1;
    RETURN (
        SELECT `Salary`
        FROM `Employee`
        GROUP BY `Salary`
        ORDER BY `Salary` DESC
        LIMIT N,1
    );
END
```