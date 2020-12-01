# LeetCode题解(1581)：进店却未进行过交易的顾客(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/customer-who-visited-but-did-not-make-any-transactions/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 902ms (57.14%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT customer_id,
       COUNT(DISTINCT visit_id) AS count_no_trans
FROM Visits
WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)
GROUP BY customer_id;
```