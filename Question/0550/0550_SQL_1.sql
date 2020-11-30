Create table If Not Exists Activity
(
    player_id int,
    device_id int,
    event_date date,
    games_played int
);

# Part1
SELECT COUNT(A3.player_id) AS c1
FROM (SELECT player_id
      FROM Activity
      GROUP BY player_id) AS A3;

# Part2
SELECT COUNT(A1.player_id) AS c2
FROM Activity AS A1
         JOIN
     Activity AS A2 ON A1.player_id = A2.player_id
WHERE A1.event_date = A2.event_date - 1
  AND (A1.player_id, A1.event_date) IN (SELECT player_id, MIN(event_date)
                                        FROM Activity
                                        GROUP BY player_id);

# Result
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