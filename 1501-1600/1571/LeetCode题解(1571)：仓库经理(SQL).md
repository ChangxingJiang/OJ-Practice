# LeetCode题解(1571)：仓库经理(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/warehouse-manager/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 437ms (44.34%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT name AS WAREHOUSE_NAME,
       SUM(Width * Length * Height * units) AS VOLUME
FROM Warehouse
         LEFT JOIN
     Products P USING (product_id)
GROUP BY name;
```