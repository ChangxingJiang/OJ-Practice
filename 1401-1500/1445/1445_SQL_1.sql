Create table If Not Exists Sales
(
    sale_date date,
    fruit ENUM ('apples', 'oranges'),
    sold_num int
);

SELECT sale_date,
       SUM(sold_num) AS value
FROM Sales
WHERE fruit = 'apples'
GROUP BY sale_date;

SELECT sale_date,
       -SUM(sold_num) AS value
FROM Sales
WHERE fruit = 'oranges'
GROUP BY sale_date;


SELECT sale_date,
       SUM(value) AS diff
FROM (SELECT sale_date,
             SUM(sold_num) AS value
      FROM Sales
      WHERE fruit = 'apples'
      GROUP BY sale_date
      UNION ALL
      SELECT sale_date,
             -SUM(sold_num) AS value
      FROM Sales
      WHERE fruit = 'oranges'
      GROUP BY sale_date) AS T
GROUP BY sale_date
ORDER BY sale_date;
