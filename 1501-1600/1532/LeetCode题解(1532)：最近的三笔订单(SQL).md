# LeetCode题解(1532)：最近的三笔订单(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/the-most-recent-three-orders/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 721ms (66.05%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT T2.name AS customer_name,
       customer_id,
       order_id,
       order_date
FROM (SELECT order_id,
             customer_id,
             row_number() over (PARTITION BY customer_id ORDER BY order_date DESC) AS id,
             order_date
      FROM Orders) AS T1
         JOIN
     Customers AS T2 USING (customer_id)
WHERE id < 4
ORDER BY customer_name, customer_id, order_date DESC;
```