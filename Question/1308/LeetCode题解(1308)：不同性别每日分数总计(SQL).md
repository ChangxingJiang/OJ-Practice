# LeetCode题解(1308)：不同性别每日分数总计(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/running-total-for-different-genders/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 839ms (26.74%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT s1.gender, s1.day, SUM(s2.score_points) AS total
FROM Scores AS s1,
     Scores AS s2
WHERE s1.gender = s2.gender
  AND s1.day >= s2.day
GROUP BY s1.gender, s1.day
ORDER BY s1.gender, s1.day;
```