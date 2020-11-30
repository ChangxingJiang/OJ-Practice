Create table Sales
(
    sale_id int,
    product_id int,
    year int,
    quantity int,
    price int
);
Create table Product
(
    product_id int,
    product_name varchar(10)
);

SELECT product_id,
       SUM(quantity) AS total_quantity
FROM Sales
GROUP BY product_id;