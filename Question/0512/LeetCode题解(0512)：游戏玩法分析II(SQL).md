# LeetCode题解(0512)：游戏玩法分析II(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/game-play-analysis-ii/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 446ms (33.19%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT player_id, device_id
FROM Activity
WHERE (player_id, event_date) IN (SELECT player_id, MIN(event_date)
                                  FROM Activity
                                  GROUP BY player_id);
```