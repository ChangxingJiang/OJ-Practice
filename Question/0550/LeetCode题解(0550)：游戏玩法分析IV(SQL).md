# LeetCode题解(0550)：游戏玩法分析IV(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/game-play-analysis-iv/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 411ms (62.38%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT ROUND(B2.c2 / B1.C1, 2) AS Fraction
FROM (SELECT COUNT(A3.player_id) AS c1
      FROM (SELECT player_id
            FROM Activity
            GROUP BY player_id) AS A3) AS B1
         JOIN
     (SELECT COUNT(A1.player_id) AS c2
      FROM Activity AS A1
               JOIN
           Activity AS A2 ON A1.player_id = A2.player_id
      WHERE A1.event_date = A2.event_date - 1
        AND (A1.player_id, A1.event_date) IN (SELECT player_id, MIN(event_date)
                                              FROM Activity
                                              GROUP BY player_id)) AS B2;
```