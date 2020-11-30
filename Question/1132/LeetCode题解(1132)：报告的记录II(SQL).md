# LeetCode题解(1132)：报告的记录II(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/reported-posts-ii/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 755ms (28.46%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT ROUND(AVG(rate), 2) AS average_daily_percent
FROM (SELECT COUNT(DISTINCT R.post_id) / COUNT(DISTINCT A.post_id) * 100 AS rate
      FROM Actions AS A
               LEFT JOIN
           Removals AS R on A.post_id = R.post_id
      WHERE A.action = 'report'
        AND A.extra = 'spam'
      GROUP BY action_date) AS T;
```