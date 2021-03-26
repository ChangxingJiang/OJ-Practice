Create table If Not Exists Products
(
    product_id int,
    new_price int,
    change_date date
);

# STEP 1
SELECT product_id, MAX(change_date)
FROM Products
WHERE change_date <= '2019-08-16'
GROUP BY product_id;

# STEP 2
SELECT product_id, new_price
FROM Products
WHERE (product_id, change_date) IN (SELECT product_id, MAX(change_date)
                                    FROM Products
                                    WHERE change_date <= '2019-08-16'
                                    GROUP BY product_id);

# STEP 3
SELECT P.product_id,
       IFNULL(T.new_price, 10) AS price
FROM Products AS P
         LEFT JOIN
     (SELECT product_id, new_price
      FROM Products
      WHERE (product_id, change_date) IN (SELECT product_id, MAX(change_date)
                                          FROM Products
                                          WHERE change_date <= '2019-08-16'
                                          GROUP BY product_id)) AS T ON P.product_id = T.product_id
GROUP BY P.product_id;
