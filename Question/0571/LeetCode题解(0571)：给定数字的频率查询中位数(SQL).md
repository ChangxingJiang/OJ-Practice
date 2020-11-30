# LeetCode题解(0571)：给定数字的频率查询中位数(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/find-median-given-frequency-of-numbers/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 483ms (28.60%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT AVG(Number) AS Median
FROM (SELECT N1.Number
      FROM Numbers AS N1
               JOIN
           Numbers AS N2 ON N1.Number >= N2.Number
      GROUP BY N1.Number
      HAVING SUM(N2.Frequency) >= (SELECT SUM(Frequency) FROM Numbers) / 2
         AND SUM(N2.Frequency) - AVG(N1.Frequency) <= (SELECT SUM(Frequency) FROM Numbers) / 2) AS T;
```