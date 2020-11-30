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
SELECT buyer_id,
       IF(product_name = 'S8', 1, 0) AS S8,
       IF(product_name = 'iPhone', 1, 0) AS iPhone
FROM Sales AS S
         left join
     Product P on S.product_id = P.product_id;


# STEP 2
SELECT buyer_id
FROM (SELECT buyer_id,
             IF(product_name = 'S8', 1, 0) AS S8,
             IF(product_name = 'iPhone', 1, 0) AS iPhone
      FROM Sales AS S
               left join
           Product P on S.product_id = P.product_id) as T
GROUP BY buyer_id
HAVING SUM(S8) > 0
   AND SUM(iPhone) = 0;