CREATE TABLE If Not Exists point_2d
(
    x INT NOT NULL,
    y INT NOT NULL
);

# STEP 1
SELECT P1.x, P1.y, P2.x, P2.y
FROM point_2d AS P1
         CROSS JOIN
     point_2d AS P2 ON P1.x != P2.x OR P1.y != P2.y;

# STEP 2
SELECT ROUND(SQRT(POW((P1.x - P2.x), 2) + POW((P1.y - P2.y), 2)), 2) AS shortest
FROM point_2d AS P1
         CROSS JOIN
     point_2d AS P2 ON P1.x != P2.x OR P1.y != P2.y
ORDER BY shortest
LIMIT 1;