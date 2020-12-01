# LeetCode题解(1251)：平均售价(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/average-selling-price/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 522ms (34.05%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT U.product_id,
       ROUND(SUM(U.units*P.price) / SUM(U.units),2) AS average_price
FROM UnitsSold AS U
         LEFT JOIN
     Prices AS P on U.product_id = P.product_id AND
                    U.purchase_date BETWEEN P.start_date AND P.end_date
GROUP BY P.product_id;
```