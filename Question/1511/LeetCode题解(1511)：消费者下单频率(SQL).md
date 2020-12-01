# LeetCode题解(1511)：消费者下单频率(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/customer-order-frequency/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 591ms (63.62%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT customer_id, name
FROM (SELECT O.customer_id,
             C.name
      FROM Orders AS O
               LEFT JOIN
           Customers C USING (customer_id)
               LEFT JOIN
           Product AS P USING (product_id)
      WHERE order_date BETWEEN '2020-06-01' AND '2020-06-30'
      GROUP BY O.customer_id
      HAVING SUM(P.price * O.quantity) >= 100
      UNION ALL
      SELECT O.customer_id,
             C.name
      FROM Orders AS O
               LEFT JOIN
           Customers C USING (customer_id)
               LEFT JOIN
           Product AS P USING (product_id)
      WHERE order_date BETWEEN '2020-07-01' AND '2020-07-31'
      GROUP BY O.customer_id
      HAVING SUM(P.price * O.quantity) >= 100) AS T
GROUP BY customer_id, name
HAVING COUNT(*) = 2;
```