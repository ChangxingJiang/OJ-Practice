Create table If Not Exists Customers
(
    customer_id int,
    customer_name varchar(20)
);

WITH RECURSIVE A AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1
    FROM A
    WHERE n < 100
)

SELECT n AS ids
FROM A
WHERE n NOT IN (SELECT customer_id FROM Customers)
  AND n <= (SELECT MAX(customer_id) FROM Customers);