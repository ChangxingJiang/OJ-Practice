Create table If Not Exists Queries
(
    query_name varchar(30),
    result varchar(50),
    position int,
    rating int
);

SELECT query_name,
       ROUND(AVG(rating / position), 2) AS quality,
       ROUND((SELECT COUNT(*) FROM Queries WHERE query_name = Q.query_name AND rating < 3)
                 /
             COUNT(*)
                 * 100, 2) AS poor_query_percentage
FROM Queries AS Q
GROUP BY query_name;