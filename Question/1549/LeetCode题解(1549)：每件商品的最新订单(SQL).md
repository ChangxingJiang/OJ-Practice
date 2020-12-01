# LeetCode题解(1549)：每件商品的最新订单(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/the-most-recent-orders-for-each-product/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) |            |            | 1636ms (27.74%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```MYSQL
SELECT product_name, product_id, order_id, order_date
FROM Orders
         LEFT JOIN
     Products USING (product_id)
WHERE (product_id, order_date) IN (SELECT product_id, MAX(order_date)
                                   FROM Orders
                                   GROUP BY product_id)
ORDER BY product_name, product_id, order_id;
```