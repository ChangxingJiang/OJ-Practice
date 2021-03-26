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
SELECT product_id
FROM Sales
GROUP BY product_id
HAVING MIN(sale_date) BETWEEN '2019-01-01' AND '2019-04-01'
   AND MAX(sale_date) BETWEEN '2019-01-01' AND '2019-04-01';

# STEP 2
SELECT S.product_id,P.product_name
FROM Sales AS S
         LEFT JOIN
     Product AS P on S.product_id = P.product_id
GROUP BY product_id
HAVING MIN(sale_date) BETWEEN '2019-01-01' AND '2019-04-01'
   AND MAX(sale_date) BETWEEN '2019-01-01' AND '2019-04-01';