Create Table If Not Exists NPV
(
    id int,
    year int,
    npv int
);
Create Table If Not Exists Queries
(
    id int,
    year int
);

SELECT Q.id,
       Q.year,
       IFNULL(N.npv, IF(Q.id = @pre_id, @val := N.npv, 0)) AS npv,
       (@pre_id := Q.id)
FROM Queries AS Q
         LEFT JOIN
     NPV AS N USING (id, year),
     (SELECT @pre_id := NULL, @val := 0) AS T
ORDER BY Q.id;

SELECT Q.id,
       Q.year,
       IFNULL(N.npv,0) AS npv
FROM Queries AS Q
         LEFT JOIN
     NPV AS N USING (id, year)
ORDER BY Q.id;