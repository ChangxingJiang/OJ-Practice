# LeetCode题解(1107)：每日新用户统计(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/new-users-daily-count/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 441ms (19.96%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT login_date, COUNT(user_id) AS user_count
FROM (SELECT user_id, MIN(activity_date) AS login_date
      FROM Traffic
      WHERE activity = 'login'
      GROUP BY user_id) AS T
WHERE DATEDIFF('2019-06-30',login_date) <= 90
GROUP BY login_date;
```