# LeetCode题解(0262)：行程和用户(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/trips-and-users/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 287ms (68.84%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT T.Request_at AS `Day`,
       ROUND(SUM(IF(T.Status = 'completed', 0, 1)) / COUNT(T.Status), 2) AS `Cancellation Rate`
FROM Trips AS T
WHERE T.Client_Id NOT IN (
    SELECT Users_Id
    FROM Users
    WHERE Banned = 'Yes'
)
  AND T.Driver_Id NOT IN (
    SELECT Users_Id
    FROM Users
    WHERE Banned = 'Yes'
)
  AND T.Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY T.Request_at;
```