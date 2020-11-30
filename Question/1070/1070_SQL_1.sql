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

# STEP 1
SELECT product_id, MIN(year) AS first_year
FROM Sales
GROUP BY product_id;

# STEP 2
SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) IN (SELECT product_id, MIN(year) AS first_year
                             FROM Sales
                             GROUP BY product_id);