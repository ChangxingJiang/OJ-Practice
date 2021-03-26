Create table If Not Exists Customers
(
    customer_id int,
    customer_name varchar(30)
);
Create table If Not Exists Orders
(
    order_id int,
    customer_id int,
    product_name varchar(30)
);

SELECT O.customer_id,
       C.customer_name
FROM Orders AS O
         LEFT JOIN
     Customers C on O.customer_id = C.customer_id
GROUP BY customer_id
HAVING SUM(product_name = 'A') > 0
   AND SUM(product_name = 'B') > 0
   AND SUM(product_name = 'C') = 0;