# LeetCode题解(0585)：2016年的投资(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/investments-in-2016/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 392ms (46.69%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT SUM(TIV_2016) AS TIV_2016
FROM insurance
WHERE (LAT, LON) IN (SELECT LAT, LON
                     FROM insurance
                     GROUP BY LAT, LON
                     HAVING COUNT(*) = 1)
  AND TIV_2015 IN (SELECT TIV_2015
                   FROM insurance
                   GROUP BY TIV_2015
                   HAVING COUNT(*) > 1);
```