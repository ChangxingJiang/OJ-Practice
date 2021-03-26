Create table If Not Exists Activity
(
    player_id int,
    device_id int,
    event_date date,
    games_played int
);

SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;