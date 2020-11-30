CREATE TABLE IF NOT EXISTS customer
(
    id INT,
    name VARCHAR(25),
    referee_id INT
);

SELECT name
FROM customer
WHERE referee_id IS NULL
   OR referee_id <> 2;