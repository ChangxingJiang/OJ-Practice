Create table If Not Exists Orders
(
    order_id int,
    order_date date,
    customer_id int,
    invoice int
);

SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
       COUNT(DISTINCT order_id) AS order_count,
       COUNT(DISTINCT customer_id) AS customer_count
FROM Orders
WHERE invoice > 20
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY month;

