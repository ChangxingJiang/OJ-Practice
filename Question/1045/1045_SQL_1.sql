Create table If Not Exists Customer
(
    customer_id int,
    product_key int
);
Create table Product
(
    product_key int
);

# STEP 1
SELECT customer_id, COUNT(DISTINCT product_key) AS num
FROM Customer
GROUP BY customer_id;

# STEP 2
SELECT T.customer_id
FROM (SELECT customer_id, COUNT(DISTINCT product_key) AS num
      FROM Customer
      GROUP BY customer_id) AS T,
     (SELECT @num := COUNT(*) FROM Product) AS C
WHERE T.num = @num;
