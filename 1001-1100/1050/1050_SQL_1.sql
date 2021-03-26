Create table If Not Exists ActorDirector
(
    actor_id int,
    director_id int,
    timestamp int
);

SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(timestamp) >= 3;