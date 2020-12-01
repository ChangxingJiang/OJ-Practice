# LeetCode题解(1384)：按年度列出销售总额(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/total-sales-amount-by-year/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) |            |            | 450ms (5.06%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```mysql
SELECT T.product_id,
       P.product_name,
       T.report_year,
       T.total_amount
FROM (SELECT product_id,
             '2018' AS report_year,
             CASE
                 WHEN period_end < '2018-01-01' OR '2018-12-31' < period_start THEN
                     0
                 WHEN period_start < '2018-01-01' AND '2018-12-31' < period_end THEN
                     365 * average_daily_sales
                 WHEN period_start < '2018-01-01' AND period_end < '2018-12-31' THEN
                     (DATEDIFF(period_end, '2018-01-01') + 1) * average_daily_sales
                 WHEN '2018-01-01' < period_start AND '2018-12-31' < period_end THEN
                     (DATEDIFF('2018-12-31', period_start) + 1) * average_daily_sales
                 WHEN '2018-01-01' < period_start AND period_end < '2018-12-31' THEN
                     (DATEDIFF(period_end, period_start) + 1) * average_daily_sales
                 END AS total_amount
      FROM Sales

      UNION ALL

      SELECT product_id,
             '2019' AS report_year,
             CASE
                 WHEN period_end < '2019-01-01' OR '2019-12-31' < period_start THEN
                     0
                 WHEN period_start < '2019-01-01' AND '2019-12-31' < period_end THEN
                     365 * average_daily_sales
                 WHEN period_start < '2019-01-01' AND period_end < '2019-12-31' THEN
                     (DATEDIFF(period_end, '2019-01-01') + 1) * average_daily_sales
                 WHEN '2019-01-01' < period_start AND '2019-12-31' < period_end THEN
                     (DATEDIFF('2019-12-31', period_start) + 1) * average_daily_sales
                 WHEN '2019-01-01' < period_start AND period_end < '2019-12-31' THEN
                     (DATEDIFF(period_end, period_start) + 1) * average_daily_sales
                 END AS total_amount
      FROM Sales

      UNION ALL

      SELECT product_id,
             '2020' AS report_year,
             CASE
                 WHEN period_end < '2020-01-01' OR '2020-12-31' < period_start THEN
                     0
                 WHEN period_start < '2020-01-01' AND '2020-12-31' < period_end THEN
                     366 * average_daily_sales
                 WHEN period_start < '2020-01-01' AND period_end < '2020-12-31' THEN
                     (DATEDIFF(period_end, '2020-01-01') + 1) * average_daily_sales
                 WHEN '2020-01-01' < period_start AND '2020-12-31' < period_end THEN
                     (DATEDIFF('2019-12-31', period_start) + 1) * average_daily_sales
                 WHEN '2020-01-01' < period_start AND period_end < '2020-12-31' THEN
                     (DATEDIFF(period_end, period_start) + 1) * average_daily_sales
                 END AS total_amount
      FROM Sales) AS T
         LEFT JOIN
     Product AS P ON P.product_id = T.product_id
WHERE total_amount > 0
ORDER BY product_id, report_year;
```