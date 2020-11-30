# LeetCode题解(1225)：报告系统状态的连续日期(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/report-contiguous-dates/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 849ms (34.83%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT period_state,
       MIN(T.date) AS start_date,
       MAX(T.date) AS end_date
FROM (SELECT success_date AS date,
             'succeeded' AS period_state,
             IF(DATEDIFF(@pre_date, @pre_date := success_date) = -1, @id, @id := @id + 1) AS id
      FROM Succeeded,
           (SELECT @id := 0, @pre_date := NULL) AS Param
      UNION
      SELECT fail_date AS date,
             'failed' AS period_state,
             IF(DATEDIFF(@pre_date, @pre_date := fail_date) = -1, @id, @id := @id + 1) AS id
      FROM Failed,
           (SELECT @id := 0, @pre_date := NULL) AS Param
     ) AS T
WHERE date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY T.id
ORDER BY start_date;
```