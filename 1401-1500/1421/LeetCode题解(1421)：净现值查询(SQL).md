# LeetCode题解(1421)：净现值查询(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/npv-queries/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 598ms (38.28%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT Q.id,
       Q.year,
       IFNULL(N.npv,0) AS npv
FROM Queries AS Q
         LEFT JOIN
     NPV AS N USING (id, year)
ORDER BY Q.id;
```