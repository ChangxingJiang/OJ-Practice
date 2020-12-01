# LeetCode题解(1555)：银行账户概要(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/bank-account-summary/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 492ms (47.48%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```MYSQL
SELECT user_id,
       user_name,
       credit + IFNULL(SUM(IF(U.user_id = T.paid_to, 1, -1) * T.amount), 0) AS credit,
       IF(credit + IFNULL(SUM(IF(U.user_id = T.paid_to, 1, -1) * T.amount), 0) >= 0, 'No',
          'Yes') AS credit_limit_breached
FROM Users AS U
         LEFT JOIN
     Transactions AS T ON U.user_id = T.paid_to OR U.user_id = T.paid_by
GROUP BY user_id;
```