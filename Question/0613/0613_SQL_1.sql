CREATE TABLE If Not Exists point
(
    x INT NOT NULL,
    UNIQUE INDEX x_UNIQUE (x ASC)
);

SELECT ABS(P1.x - P2.x) AS shortest
FROM point AS P1
         CROSS JOIN
     point AS P2 ON P1.x != P2.x
ORDER BY shortest
LIMIT 1;