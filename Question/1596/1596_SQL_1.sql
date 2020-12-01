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
    product_id int
);
Create table If Not Exists Products
(
    product_id int,
    product_name varchar(20),
    price int
);

SELECT customer_id, COUNT(order_id) AS times
FROM Orders
GROUP BY customer_id, product_id;

SELECT customer_id, MAX(times)
FROM (SELECT customer_id, COUNT(order_id) AS times
      FROM Orders
      GROUP BY customer_id, product_id) AS T1
GROUP BY customer_id;

SELECT customer_id, product_id, product_name
FROM Orders
         LEFT JOIN
     Products USING (product_id)
GROUP BY customer_id, product_id
HAVING (customer_id, COUNT(order_id)) IN (
    SELECT customer_id, MAX(times)
    FROM (SELECT customer_id, COUNT(order_id) AS times
          FROM Orders
          GROUP BY customer_id, product_id) AS T1
    GROUP BY customer_id);

