# LeetCode题解(1336)：每次访问的交易次数(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-transactions-per-visit/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) |            |            | 841ms (5.12%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```mysql
SELECT 0 AS transactions_count,
       COUNT(*) AS visits_count
FROM (
         SELECT user_id, visit_date
         FROM Visits
         WHERE (user_id, visit_date) NOT IN
               (SELECT user_id, transaction_date FROM Transactions)
     ) AS T1
UNION ALL
SELECT T2.id AS transactions_count,
       IFNULL(T3.visits_count, 0) AS visits_count
FROM (
         SELECT id
         FROM (SELECT (@x := @x + 1) AS id
               FROM Transactions,
                    (SELECT @x := 0) AS ID) AS T4
         WHERE id <= (
             SELECT max(transactions_count)
             FROM (
                      SELECT count(*) AS transactions_count
                      FROM Transactions
                      GROUP BY user_id, transaction_date
                  ) AS T5
         )
     ) T2
         LEFT JOIN
     (
         SELECT transactions_count,
                COUNT(transactions_count) AS visits_count
         FROM (
                  SELECT count(*) AS transactions_count
                  FROM Transactions
                  GROUP BY user_id, transaction_date
              ) AS T6
         GROUP BY transactions_count
     ) T3
     ON T2.id = T3.transactions_count
ORDER BY transactions_count;
```