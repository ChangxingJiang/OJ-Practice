# LeetCode题解(1212)：查询球队积分(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/team-scores-in-football-tournament/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 518ms (72.36%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT U.team_id,
       Teams.team_name,
       IFNULL(SUM(U.score), 0) AS num_points
FROM (SELECT T.team_id,
             IFNULL(SUM(M.host_score),0) AS score
      FROM Teams AS T
               LEFT JOIN
           (SELECT match_id,
                   host_team,
                   guest_team,
                   CASE
                       WHEN host_goals > guest_goals THEN 3
                       WHEN host_goals = guest_goals THEN 1
                       ELSE 0
                       END AS host_score,
                   CASE
                       WHEN host_goals > guest_goals THEN 0
                       WHEN host_goals = guest_goals THEN 1
                       ELSE 3
                       END AS guest_score
            FROM Matches) AS M ON T.team_id = M.host_team
      GROUP BY T.team_id
      UNION ALL
      SELECT T.team_id,
             IFNULL(SUM(M.guest_score),0) AS score
      FROM Teams AS T
               LEFT JOIN
           (SELECT match_id,
                   host_team,
                   guest_team,
                   CASE
                       WHEN host_goals > guest_goals THEN 3
                       WHEN host_goals = guest_goals THEN 1
                       ELSE 0
                       END AS host_score,
                   CASE
                       WHEN host_goals > guest_goals THEN 0
                       WHEN host_goals = guest_goals THEN 1
                       ELSE 3
                       END AS guest_score
            FROM Matches) AS M ON T.team_id = M.guest_team
      GROUP BY T.team_id) AS U
         LEFT JOIN
     Teams ON Teams.team_id = U.team_id
GROUP BY team_id
ORDER BY num_points DESC, team_id;
```