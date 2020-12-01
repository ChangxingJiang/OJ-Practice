# LeetCode题解(1327)：列出指定时间段内所有的下单产品(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/list-the-products-ordered-in-a-period/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 422ms (87.04%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT P.product_name,
       IFNULL(T.unit, 0) AS unit
FROM Products AS P
         LEFT JOIN
     (SELECT product_id, SUM(unit) AS unit
      FROM Orders
      WHERE order_date BETWEEN '2020-02-01' AND '2020-02-29'
      GROUP BY product_id) AS T ON P.product_id = T.product_id
WHERE unit >= 100;
```