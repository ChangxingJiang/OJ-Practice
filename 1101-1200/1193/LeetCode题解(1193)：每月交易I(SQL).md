# LeetCode题解(1193)：每月交易I(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/monthly-transactions-i/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 567ms (10.16%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT T1.month,
       T1.country,
       T1.trans_count,
       IFNULL(T2.approved_count, 0) AS approved_count,
       T1.trans_total_amount,
       IFNULL(T2.approved_total_amount, 0) AS approved_total_amount
FROM (SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
             country,
             COUNT(id) AS trans_count,
             SUM(amount) AS trans_total_amount
      FROM Transactions
      GROUP BY country, DATE_FORMAT(trans_date, '%Y-%m')) AS T1
         LEFT JOIN
     (SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
             country,
             COUNT(id) AS approved_count,
             SUM(amount) AS approved_total_amount
      FROM Transactions
      WHERE state = 'approved'
      GROUP BY country, DATE_FORMAT(trans_date, '%Y-%m')) AS T2
     ON T1.month = T2.month AND T1.country = T2.country;
```