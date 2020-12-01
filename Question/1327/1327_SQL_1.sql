Create table If Not Exists Products
(
    product_id int,
    product_name varchar(40),
    product_category varchar(40)
);
Create table If Not Exists Orders
(
    product_id int,
    order_date date,
    unit int
);

SELECT product_id, SUM(unit) AS unit
FROM Orders
WHERE order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY product_id;

SELECT P.product_name,
       IFNULL(T.unit, 0) AS unit
FROM Products AS P
         LEFT JOIN
     (SELECT product_id, SUM(unit) AS unit
      FROM Orders
      WHERE order_date BETWEEN '2020-02-01' AND '2020-02-29'
      GROUP BY product_id) AS T ON P.product_id = T.product_id
WHERE unit >= 100;

