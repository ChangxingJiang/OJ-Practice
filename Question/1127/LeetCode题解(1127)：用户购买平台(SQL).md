# LeetCode题解(1127)：用户购买平台(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/user-purchase-platform/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 470ms (37.76%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT DISTINCT S.spend_date,
                P.platform,
                IFNULL(T.total_amount,0) AS total_amount,
                IFNULL(T.total_users,0) AS total_users
FROM Spending AS S
         CROSS JOIN
     (SELECT 'mobile' AS platform
      UNION
      SELECT 'desktop' AS platform
      UNION
      SELECT 'both' AS platform) AS P
         LEFT JOIN
     (SELECT spend_date,
             platform,
             SUM(amount) AS total_amount,
             COUNT(DISTINCT user_id) AS total_users
      FROM (SELECT user_id,
                   spend_date,
                   IF(COUNT(DISTINCT platform) = 1, platform, 'both') AS platform,
                   SUM(amount) AS amount
            FROM Spending
            GROUP BY user_id, spend_date) AS T
      GROUP BY spend_date, platform) AS T ON T.spend_date = S.spend_date AND T.platform = P.platform;
```