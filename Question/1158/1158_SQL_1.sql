Create table If Not Exists Users
(
    user_id int,
    join_date date,
    favorite_brand varchar(10)
);
create table if not exists Orders
(
    order_id int,
    order_date date,
    item_id int,
    buyer_id int,
    seller_id int
);
create table if not exists Items
(
    item_id int,
    item_brand varchar(10)
);

# STEP 1
SELECT buyer_id, COUNT(order_id) AS orders_in_2019
FROM Orders
WHERE YEAR(order_date) = 2019
GROUP BY buyer_id;

# STEP 2
SELECT user_id AS buyer_id,
       join_date,
       IFNULL(orders_in_2019, 0) AS orders_in_2019
FROM Users AS U
         LEFT JOIN
     (SELECT buyer_id, COUNT(order_id) AS orders_in_2019
      FROM Orders
      WHERE YEAR(order_date) = 2019
      GROUP BY buyer_id) AS T ON U.user_id = T.buyer_id;
