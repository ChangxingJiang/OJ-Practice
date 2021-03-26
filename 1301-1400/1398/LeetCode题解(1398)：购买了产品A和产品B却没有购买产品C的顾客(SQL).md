# LeetCode题解(1398)：购买了产品A和产品B却没有购买产品C的顾客(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/customers-who-bought-products-a-and-b-but-not-c/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) |            |            | 535ms (8.65%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```mysql
SELECT O.customer_id,
       C.customer_name
FROM Orders AS O
         LEFT JOIN
     Customers C on O.customer_id = C.customer_id
GROUP BY customer_id
HAVING SUM(product_name = 'A') > 0
   AND SUM(product_name = 'B') > 0
   AND SUM(product_name = 'C') = 0;
```