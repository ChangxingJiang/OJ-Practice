# LeetCode题解(1587)：银行账户概要II(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/bank-account-summary-ii/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 535ms (23.21%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT name,
       SUM(amount) AS balance
FROM Users
         LEFT JOIN
     Transactions USING (account)
GROUP BY account
HAVING balance > 10000;
```