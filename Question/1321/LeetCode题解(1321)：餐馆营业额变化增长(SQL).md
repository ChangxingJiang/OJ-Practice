# LeetCode题解(1321)：餐馆营业额变化增长(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/restaurant-growth/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 326ms (49.54%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT C1.visited_on,
       SUM(C2.amount) AS amount,
       ROUND(SUM(C2.amount) / 7, 2) AS average_amount
FROM (SELECT DISTINCT visited_on FROM Customer) AS C1
         LEFT JOIN
     Customer AS C2 ON DATEDIFF(C1.visited_on, C2.visited_on) BETWEEN 0 AND 6
WHERE C1.visited_on >= (SELECT MIN(visited_on) FROM Customer) + 6
GROUP BY C1.visited_on
ORDER BY C1.visited_on;
```