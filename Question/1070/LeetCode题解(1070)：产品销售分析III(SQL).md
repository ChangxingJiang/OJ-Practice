# LeetCode题解(1070)：产品销售分析III(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/product-sales-analysis-iii/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 1153ms (5.08%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) IN (SELECT product_id, MIN(year) AS first_year
                             FROM Sales
                             GROUP BY product_id);
```