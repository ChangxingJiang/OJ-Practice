# LeetCode题解(1651)：Hopper Company Queries III(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/hopper-company-queries-iii/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) |            |            | 1126ms (51.28%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```mysql
WITH RECURSIVE MonthList AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1
    FROM MonthList
    WHERE month < 10
)
SELECT L.month,
       ROUND(IFNULL(SUM(ride_distance) / 3, 0), 2) AS average_ride_distance,
       ROUND(IFNULL(SUM(ride_duration) / 3, 0), 2) AS average_ride_duration
FROM MonthList AS L
         LEFT JOIN
     (
         SELECT *
         FROM Rides AS R
                  LEFT JOIN
              AcceptedRides USING (ride_id)
         WHERE YEAR(requested_at) = 2020
     ) AS T ON L.month - MONTH(requested_at) BETWEEN -2 AND 0
GROUP BY month
ORDER BY month;
```