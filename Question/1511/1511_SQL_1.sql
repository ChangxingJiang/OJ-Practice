Create table If Not Exists Customers
(
    customer_id int,
    name varchar(30),
    country varchar(30)
);
Create table If Not Exists Product
(
    product_id int,
    description varchar(30),
    price int
);
Create table If Not Exists Orders
(
    order_id int,
    customer_id int,
    product_id int,
    order_date date,
    quantity int
);

SELECT customer_id, name
FROM (SELECT O.customer_id,
             C.name
      FROM Orders AS O
               LEFT JOIN
           Customers C USING (customer_id)
               LEFT JOIN
           Product AS P USING (product_id)
      WHERE order_date BETWEEN '2020-06-01' AND '2020-06-30'
      GROUP BY O.customer_id
      HAVING SUM(P.price * O.quantity) >= 100
      UNION ALL
      SELECT O.customer_id,
             C.name
      FROM Orders AS O
               LEFT JOIN
           Customers C USING (customer_id)
               LEFT JOIN
           Product AS P USING (product_id)
      WHERE order_date BETWEEN '2020-07-01' AND '2020-07-31'
      GROUP BY O.customer_id
      HAVING SUM(P.price * O.quantity) >= 100) AS T
GROUP BY customer_id, name
HAVING COUNT(*) = 2;