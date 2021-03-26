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

SELECT product_id, MAX(order_date)
FROM Orders
GROUP BY product_id;

SELECT product_name, product_id, order_id, order_date
FROM Orders
         LEFT JOIN
     Products USING (product_id)
WHERE (product_id, order_date) IN (SELECT product_id, MAX(order_date)
                                   FROM Orders
                                   GROUP BY product_id)
ORDER BY product_name, product_id, order_id;
