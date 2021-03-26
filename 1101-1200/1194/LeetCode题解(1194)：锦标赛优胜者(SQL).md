# LeetCode题解(1194)：锦标赛优胜者(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/tournament-winners/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 572ms (65.52%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT group_id, player_id
FROM (SELECT group_id, player_id, SUM(score) AS score
      FROM (SELECT P.player_id, P.group_id, M.first_score AS score
            FROM Players AS P
                     JOIN
                 Matches AS M ON P.player_id = M.first_player
            UNION ALL
            SELECT P.player_id, P.group_id, M.second_score AS score
            FROM Players AS P
                     JOIN
                 Matches AS M ON P.player_id = M.second_player) as T1
      GROUP BY player_id
      ORDER BY score DESC, player_id) as T2
GROUP BY group_id;
```