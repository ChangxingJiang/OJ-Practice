Create table If Not Exists Customer
(
    customer_id int,
    name varchar(20),
    visited_on date,
    amount int
);

SELECT C1.visited_on,
       SUM(C2.amount) AS amount,
       ROUND(SUM(C2.amount) / 7, 2) AS average_amount
FROM (SELECT DISTINCT visited_on FROM Customer) AS C1
         LEFT JOIN
     Customer AS C2 ON DATEDIFF(C1.visited_on, C2.visited_on) BETWEEN 0 AND 6
WHERE C1.visited_on >= (SELECT MIN(visited_on) FROM Customer) + 6
GROUP BY C1.visited_on
ORDER BY C1.visited_on;

