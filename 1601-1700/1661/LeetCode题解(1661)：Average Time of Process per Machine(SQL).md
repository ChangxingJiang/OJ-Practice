# LeetCode题解(1661)：Average Time of Process per Machine(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/average-time-of-process-per-machine/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 193ms (45.35%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT machine_id,
       ROUND(AVG(processing_time), 3) AS processing_time
FROM (
         SELECT machine_id, MAX(timestamp) - MIN(timestamp) AS processing_time
         FROM Activity
         GROUP BY machine_id, process_id
     ) AS T
GROUP BY machine_id;
```