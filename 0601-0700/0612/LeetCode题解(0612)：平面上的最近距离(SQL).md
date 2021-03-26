# LeetCode题解(0612)：平面上的最近距离(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/shortest-distance-in-a-plane/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 187ms (45.22%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT ROUND(SQRT(POW((P1.x - P2.x), 2) + POW((P1.y - P2.y), 2)), 2) AS shortest
FROM point_2d AS P1
         CROSS JOIN
     point_2d AS P2 ON P1.x != P2.x OR P1.y != P2.y
ORDER BY shortest
LIMIT 1;
```