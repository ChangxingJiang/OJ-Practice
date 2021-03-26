# LeetCode题解(1205)：每月交易II(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/monthly-transactions-ii/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) |            |            | 640ms (5.01%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```mysql
SELECT T.month,
       T.country,
       MAX(T.approved_count) AS approved_count,
       MAX(T.approved_amount) AS approved_amount,
       MAX(T.chargeback_count) AS chargeback_count,
       MAX(T.chargeback_amount) AS chargeback_amount
FROM (SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
             country,
             COUNT(id) AS approved_count,
             SUM(amount) AS approved_amount,
             0 AS chargeback_count,
             0 AS chargeback_amount
      FROM Transactions
      WHERE state = 'approved'
      GROUP BY country, DATE_FORMAT(trans_date, '%Y-%m')

      UNION

      SELECT DATE_FORMAT(C.trans_date, '%Y-%m') AS month,
             TT.country,
             0 AS approved_count,
             0 AS approved_amount,
             COUNT(TT.id) AS chargeback_count,
             SUM(TT.amount) AS chargeback_amount
      FROM Chargebacks AS C
               LEFT JOIN
           (SELECT id, country, amount
            FROM Transactions) AS TT ON C.trans_id = TT.id
      GROUP BY TT.country, DATE_FORMAT(C.trans_date, '%Y-%m')) AS T
GROUP BY T.country, T.month;
```