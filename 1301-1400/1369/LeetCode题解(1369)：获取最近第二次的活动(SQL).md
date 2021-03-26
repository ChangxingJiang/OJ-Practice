# LeetCode题解(1369)：获取最近第二次的活动(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/get-the-second-most-recent-activity/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) |            |            | 373ms (5.14%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```mysql
SELECT username, activity, startDate, endDate
FROM UserActivity
WHERE (username, startDate) IN (SELECT username, max(startDate)
                                FROM UserActivity
                                WHERE (username, startDate) NOT IN (SELECT username, max(startDate)
                                                                    FROM UserActivity
                                                                    GROUP BY username
                                                                    HAVING COUNT(username) > 1)
                                GROUP BY username);
```