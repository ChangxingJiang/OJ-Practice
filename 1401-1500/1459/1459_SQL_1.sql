Create table If Not Exists Points
(
    id int,
    x_value int,
    y_value int
);

SELECT L1.id AS p1,
       L2.id AS p2,
       ABS((L2.y_value - L1.y_value) * (L2.x_value - l1.x_value)) AS area
FROM Points AS L1,
     Points AS L2
WHERE L2.id > L1.id
  AND ABS((L2.y_value - L1.y_value) * (L2.x_value - l1.x_value)) > 0
ORDER BY area DESC, p1, p2;
