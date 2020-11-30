# LeetCode题解(1069)：产品销售分析II(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/product-sales-analysis-ii/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 1080ms (8.80%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT product_id, 
       SUM(quantity) AS total_quantity
FROM Sales
GROUP BY product_id;
```

