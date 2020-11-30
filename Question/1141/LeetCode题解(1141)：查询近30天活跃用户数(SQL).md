# LeetCode题解(1141)：查询近30天活跃用户数(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/user-activity-for-the-past-30-days-i/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 325ms (76.63%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT activity_date AS day,
       COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE DATEDIFF('2019-07-27', activity_date) < 30
GROUP BY activity_date
HAVING active_users > 0;
```