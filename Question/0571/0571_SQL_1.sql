Create table If Not Exists Numbers
(
    Number int,
    Frequency int
);

SELECT AVG(Number) AS Median
FROM (SELECT N1.Number
      FROM Numbers AS N1
               JOIN
           Numbers AS N2 ON N1.Number >= N2.Number
      GROUP BY N1.Number
      HAVING SUM(N2.Frequency) >= (SELECT SUM(Frequency) FROM Numbers) / 2
         AND SUM(N2.Frequency) - AVG(N1.Frequency) <= (SELECT SUM(Frequency) FROM Numbers) / 2) AS T;
