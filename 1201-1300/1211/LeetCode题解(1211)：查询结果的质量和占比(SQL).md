# LeetCode题解(1211)：查询结果的质量和占比(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/queries-quality-and-percentage/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) |            |            | 672ms (5.15%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```mysql
SELECT query_name,
       ROUND(AVG(rating / position), 2) AS quality,
       ROUND((SELECT COUNT(*) FROM Queries WHERE query_name = Q.query_name AND rating < 3)
                 /
             COUNT(*)
                 * 100, 2) AS poor_query_percentage
FROM Queries AS Q
GROUP BY query_name;
```