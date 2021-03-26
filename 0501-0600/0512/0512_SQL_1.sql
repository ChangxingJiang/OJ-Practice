Create table If Not Exists Activity
(
    player_id int,
    device_id int,
    event_date date,
    games_played int
);

SELECT player_id, device_id
FROM Activity
WHERE (player_id, event_date) IN (SELECT player_id, MIN(event_date)
                                  FROM Activity
                                  GROUP BY player_id);
