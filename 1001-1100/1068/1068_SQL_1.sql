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

SELECT product_name, year, price
FROM Sales
         LEFT JOIN
     Product P on Sales.product_id = P.product_id;
