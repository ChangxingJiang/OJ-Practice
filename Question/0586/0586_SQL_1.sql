Create table If Not Exists orders
(
    order_number int,
    customer_number int,
    order_date date,
    required_date date,
    shipped_date date,
    status char(15),
    comment char(200),
    key (order_number)
);

SELECT customer_number
FROM orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;

