# LeetCode题解(1113)：报告的记录(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/reported-posts/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 451ms (33.88%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT extra AS report_reason,
       COUNT(DISTINCT post_id) AS report_count
FROM Actions
WHERE DATEDIFF('2019-07-05', action_date) = 1
  AND action = 'report'
GROUP BY extra;
```