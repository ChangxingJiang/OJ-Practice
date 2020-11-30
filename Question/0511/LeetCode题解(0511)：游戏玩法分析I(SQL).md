# LeetCode题解(0511)：游戏玩法分析I(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/game-play-analysis-i/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 402ms (74.07%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
```

