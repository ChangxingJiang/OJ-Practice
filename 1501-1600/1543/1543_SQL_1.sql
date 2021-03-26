Create table If Not Exists Sales
(
    sale_id int,
    product_name varchar(30),
    sale_date date
);

SELECT LOWER(TRIM(product_name)) AS product_name,
       DATE_FORMAT(sale_date, '%Y-%m') AS sale_date,
       COUNT(sale_id) AS total
FROM Sales
GROUP BY LOWER(TRIM(product_name)), DATE_FORMAT(sale_date, '%Y-%m')
ORDER BY product_name, sale_date;