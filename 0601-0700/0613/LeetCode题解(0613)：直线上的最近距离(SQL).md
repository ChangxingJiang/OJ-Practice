# LeetCode题解(0613)：直线上的最近距离(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/shortest-distance-in-a-line/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 200ms (57.58%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT ABS(P1.x - P2.x) AS shortest
FROM point AS P1
         CROSS JOIN
     point AS P2 ON P1.x != P2.x
ORDER BY shortest
LIMIT 1;
```