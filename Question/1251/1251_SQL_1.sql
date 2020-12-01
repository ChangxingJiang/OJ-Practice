Create table If Not Exists Prices
(
    product_id int,
    start_date date,
    end_date date,
    price int
);
Create table If Not Exists UnitsSold
(
    product_id int,
    purchase_date date,
    units int
);

# STEP 1
SELECT U.product_id,
       U.purchase_date,
       U.units,
       P.price
FROM UnitsSold AS U
         LEFT JOIN
     Prices AS P on U.product_id = P.product_id AND
                    U.purchase_date BETWEEN P.start_date AND P.end_date;

# STEP 2
SELECT U.product_id,
       ROUND(SUM(U.units*P.price) / SUM(U.units),2) AS average_price
FROM UnitsSold AS U
         LEFT JOIN
     Prices AS P on U.product_id = P.product_id AND
                    U.purchase_date BETWEEN P.start_date AND P.end_date
GROUP BY P.product_id;