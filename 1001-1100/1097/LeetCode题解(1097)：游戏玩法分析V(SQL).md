# LeetCode题解(1097)：游戏玩法分析V(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/game-play-analysis-v/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 437ms (34.01%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT A1.install_dt,
       COUNT(A1.player_id) AS installs,
       round(COUNT(a2.player_id) / COUNT(a1.player_id), 2) AS Day1_retention
FROM (
         SELECT player_id, MIN(event_date) AS install_dt
         FROM Activity
         GROUP BY player_id
     ) AS A1
         LEFT JOIN
     Activity AS A2 ON (A1.player_id = A2.player_id AND A2.event_date = A1.install_dt + 1)
GROUP BY A1.install_dt;
```