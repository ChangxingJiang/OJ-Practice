# LeetCode题解(1082)：销售分析I(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/sales-analysis-i/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 861ms (52.82%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT seller_id
FROM (SELECT @max_price := (SELECT SUM(price) AS total_price
                            FROM Sales
                            GROUP BY seller_id
                            ORDER BY total_price DESC
                            LIMIT 1)) as T,
     Sales
GROUP BY seller_id
HAVING SUM(price) = @max_price;
```