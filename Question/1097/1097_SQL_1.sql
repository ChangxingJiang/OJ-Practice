Create table If Not Exists Activity
(
    player_id int,
    device_id int,
    event_date date,
    games_played int
);

# STEP 1
SELECT A1.player_id,
       IF(A2.event_date IS NOT NULL, 1, 0) AS retention
FROM Activity AS A1
         LEFT JOIN
     Activity AS A2 ON (A1.player_id = A2.player_id AND A2.event_date = A1.event_date + 1)
GROUP BY player_id;

# STEP 2
SELECT player_id, MIN(event_date) AS install_dt
FROM Activity
GROUP BY player_id;

# STEP 3
SELECT A1.install_dt,
       COUNT(A1.player_id) AS installs,
       round(COUNT(a2.player_id) / COUNT(a1.player_id), 2) AS Day1_retention
FROM (
         SELECT player_id, MIN(event_date) AS install_dt
         FROM Activity
         GROUP BY player_id
     ) AS A1
         LEFT JOIN
     Activity AS A2 ON (A1.player_id = A2.player_id AND A2.event_date = A1.install_dt + 1)
GROUP BY A1.install_dt;


# SELECT event_date, COUNT(event_date) AS installs
# FROM (SELECT MIN(event_date) AS event_date
#       FROM Activity
#       GROUP BY player_id) AS M
# GROUP BY event_date;

# SELECT Activity.event_date AS install_dt,
#        T2.installs AS installs,
#        ROUND(SUM(T1.retention) / T2.installs, 2) AS Day1_retention
# FROM Activity
#          LEFT JOIN
#      (SELECT A1.player_id,
#              IF(A2.event_date IS NOT NULL, 1, 0) AS retention
#       FROM Activity AS A1
#                LEFT JOIN
#            Activity AS A2 ON (A1.player_id = A2.player_id AND A2.event_date = A1.event_date + 1)
#       GROUP BY player_id) AS T1 ON Activity.player_id = T1.player_id
#          LEFT JOIN
#      (SELECT event_date,
#              COUNT(event_date) AS installs
#       FROM (SELECT MIN(event_date) AS event_date
#             FROM Activity
#             GROUP BY player_id) AS M
#       GROUP BY event_date) AS T2 ON Activity.event_date = T2.event_date
# WHERE Activity.event_date IN (SELECT event_date
#                               FROM (SELECT MIN(event_date) AS event_date
#                                     FROM Activity
#                                     GROUP BY player_id) AS M
#                               GROUP BY event_date)
# GROUP BY Activity.event_date
# ORDER BY Activity.event_date;


