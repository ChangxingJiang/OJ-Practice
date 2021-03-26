Create table If Not Exists Teams
(
    team_id int,
    team_name varchar(30)
);
Create table If Not Exists Matches
(
    match_id int,
    host_team int,
    guest_team int,
    host_goals int,
    guest_goals int
);

# Step 1
SELECT match_id,
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
FROM Matches;

# Step 2
SELECT T.team_id,
       SUM(M.host_score) AS score
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
GROUP BY T.team_id;

# Step 3
SELECT T.team_id,
       SUM(M.guest_score) AS score
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
GROUP BY T.team_id;

# Step 4
SELECT T.team_id,
       SUM(M.host_score) AS score
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
       SUM(M.guest_score) AS score
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
GROUP BY T.team_id;

# Step 5
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
