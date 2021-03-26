Create table If Not Exists Players
(
    player_id int,
    group_id int
);
Create table If Not Exists Matches
(
    match_id int,
    first_player int,
    second_player int,
    first_score int,
    second_score int
);

# STEP 1
SELECT P.player_id, P.group_id, M.first_score AS score
FROM Players AS P
         JOIN
     Matches AS M ON P.player_id = M.first_player;

# STEP 2
SELECT P.player_id, P.group_id, M.second_score AS score
FROM Players AS P
         JOIN
     Matches AS M ON P.player_id = M.second_player;

# STEP 3
SELECT group_id, player_id, SUM(score) AS score
FROM (SELECT P.player_id, P.group_id, M.first_score AS score
      FROM Players AS P
               JOIN
           Matches AS M ON P.player_id = M.first_player
      UNION ALL
      SELECT P.player_id, P.group_id, M.second_score AS score
      FROM Players AS P
               JOIN
           Matches AS M ON P.player_id = M.second_player) as T
GROUP BY player_id;

# STEP 4
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
