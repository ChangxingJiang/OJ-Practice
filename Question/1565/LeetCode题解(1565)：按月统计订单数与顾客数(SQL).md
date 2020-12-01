# LeetCode题解(1565)：按月统计订单数与顾客数(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/unique-orders-and-customers-per-month/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 484ms (26.82%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
       COUNT(DISTINCT order_id) AS order_count,
       COUNT(DISTINCT customer_id) AS customer_count
FROM Orders
WHERE invoice > 20
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY month;
```