# LeetCode题解(1045)：买下所有产品的客户(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/customers-who-bought-all-products/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 480ms (22.31%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT T.customer_id
FROM (SELECT customer_id, COUNT(DISTINCT product_key) AS num
      FROM Customer
      GROUP BY customer_id) AS T,
     (SELECT @num := COUNT(*) FROM Product) AS C
WHERE T.num = @num;
```