Create table If Not Exists Customers
(
    customer_id int,
    name varchar(10)
);
Create table If Not Exists Orders
(
    order_id int,
    order_date date,
    customer_id int,
    cost int
);

SELECT order_id,
       customer_id,
       row_number() over (PARTITION BY customer_id ORDER BY order_date DESC) AS id,
       order_date
FROM Orders;

SELECT T2.name AS customer_name,
       customer_id,
       order_id,
       order_date
FROM (SELECT order_id,
             customer_id,
             row_number() over (PARTITION BY customer_id ORDER BY order_date DESC) AS id,
             order_date
      FROM Orders) AS T1
         JOIN
     Customers AS T2 USING (customer_id)
WHERE id < 4
ORDER BY customer_name, customer_id, order_date DESC;
