# LeetCode题解(1596)：每位顾客最经常订购的商品(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/the-most-frequently-ordered-products-for-each-customer/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) |            |            | 1791ms (10.53%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```mysql
SELECT customer_id, product_id, product_name
FROM Orders
         LEFT JOIN
     Products USING (product_id)
GROUP BY customer_id, product_id
HAVING (customer_id, COUNT(order_id)) IN (
    SELECT customer_id, MAX(times)
    FROM (SELECT customer_id, COUNT(order_id) AS times
          FROM Orders
          GROUP BY customer_id, product_id) AS T1
    GROUP BY customer_id);
```