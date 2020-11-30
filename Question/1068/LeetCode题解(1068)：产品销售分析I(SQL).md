# LeetCode题解(1068)：产品销售分析I(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/product-sales-analysis-i/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 982ms (59.68%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT product_name, year, price
FROM Sales
         LEFT JOIN
     Product P on Sales.product_id = P.product_id;
```