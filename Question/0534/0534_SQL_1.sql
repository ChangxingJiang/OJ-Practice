Create table If Not Exists Activity
(
    player_id int,
    device_id int,
    event_date date,
    games_played int
);

SELECT A1.player_id,
       A1.event_date,
       sum(A2.games_played) AS games_played_so_far
FROM Activity AS A1
         JOIN
     Activity AS A2 ON A1.player_id = A2.player_id
WHERE A1.event_date >= A2.event_date
GROUP BY A1.player_id, A1.event_date;