Create table If Not Exists Scores
(
    player_name varchar(20),
    gender varchar(1),
    day date,
    score_points int
);

SELECT s1.gender, s1.day, SUM(s2.score_points) AS total
FROM Scores AS s1,
     Scores AS s2
WHERE s1.gender = s2.gender
  AND s1.day >= s2.day
GROUP BY s1.gender, s1.day
ORDER BY s1.gender, s1.day;