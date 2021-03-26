# LeetCode题解(0534)：游戏玩法分析III(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/game-play-analysis-iii/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 609ms (58.56%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT A1.player_id,
       A1.event_date,
       sum(A2.games_played) AS games_played_so_far
FROM Activity AS A1
         JOIN
     Activity AS A2 ON A1.player_id = A2.player_id
WHERE A1.event_date >= A2.event_date
GROUP BY A1.player_id, A1.event_date;
```