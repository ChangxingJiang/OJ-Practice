# LeetCode题解(1454)：活跃用户(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/active-users/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) |            |            | 1129ms (21.59%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```mysql
SELECT DISTINCT L1.id,
                A.name
FROM Logins AS L1
         LEFT JOIN
     Logins AS L2 ON L1.id = L2.id AND
                     DATEDIFF(L1.login_date, L2.login_date) BETWEEN 0 AND 4
         LEFT JOIN
     Accounts AS A ON L1.id = A.id
GROUP BY L1.id, L1.login_date
HAVING COUNT(DISTINCT L2.login_date) = 5;
```