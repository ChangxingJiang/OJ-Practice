# LeetCode题解(1633)：各赛事的用户注册率(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/percentage-of-users-attended-a-contest/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 729ms (74.11%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT contest_id,
       ROUND(COUNT(DISTINCT user_id) / (SELECT COUNT(user_id) FROM Users) * 100, 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id;
```