# LeetCode题解(1083)：销售分析II(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/sales-analysis-ii/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 971ms (16.85%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT buyer_id
FROM (SELECT buyer_id,
             IF(product_name = 'S8', 1, 0) AS S8,
             IF(product_name = 'iPhone', 1, 0) AS iPhone
      FROM Sales AS S
               left join
           Product P on S.product_id = P.product_id) as T
GROUP BY buyer_id
HAVING SUM(S8) > 0
   AND SUM(iPhone) = 0;
```