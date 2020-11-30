# LeetCode题解(1084)：销售分析III(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/sales-analysis-iii/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 969ms (17.15%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT S.product_id,P.product_name
FROM Sales AS S
         LEFT JOIN
     Product AS P on S.product_id = P.product_id
GROUP BY product_id
HAVING MIN(sale_date) BETWEEN '2019-01-01' AND '2019-04-01'
   AND MAX(sale_date) BETWEEN '2019-01-01' AND '2019-04-01';
```