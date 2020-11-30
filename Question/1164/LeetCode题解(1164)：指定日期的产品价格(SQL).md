# LeetCode题解(1164)：指定日期的产品价格(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/product-price-at-a-given-date/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 359ms (32.63%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT P.product_id,
       IFNULL(T.new_price, 10) AS price
FROM Products AS P
         LEFT JOIN
     (SELECT product_id, new_price
      FROM Products
      WHERE (product_id, change_date) IN (SELECT product_id, MAX(change_date)
                                          FROM Products
                                          WHERE change_date <= '2019-08-16'
                                          GROUP BY product_id)) AS T ON P.product_id = T.product_id
GROUP BY P.product_id;
```