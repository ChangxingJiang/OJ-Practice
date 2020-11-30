Create table If Not Exists Product
(
    product_id int,
    product_name varchar(10),
    unit_price int
);
Create table If Not Exists Sales
(
    seller_id int,
    product_id int,
    buyer_id int,
    sale_date date,
    quantity int,
    price int
);

# STEP 1
SELECT SUM(price) AS total_price
FROM Sales
GROUP BY seller_id
ORDER BY total_price DESC
LIMIT 1;

# STEP 2
SELECT seller_id
FROM (SELECT @max_price := (SELECT SUM(price) AS total_price
                            FROM Sales
                            GROUP BY seller_id
                            ORDER BY total_price DESC
                            LIMIT 1)) as T,
     Sales
GROUP BY seller_id
HAVING SUM(price) = @max_price;