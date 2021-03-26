# LeetCode题解(0570)：至少有5名直接下属的经理(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/managers-with-at-least-5-direct-reports/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 221ms (86.72%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT Name
FROM Employee
WHERE Id IN (
    SELECT ManagerId
    FROM Employee
    GROUP BY ManagerId
    HAVING COUNT(`Name`) >= 5);
```