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
SELECT seller_id, item_id
FROM Orders
WHERE seller_id = 2
ORDER BY order_date
LIMIT 1,1;

# STEP 2
SELECT DISTINCT O.seller_id,
                (SELECT item_id
                 FROM Orders
                 WHERE seller_id = O.seller_id
                 ORDER BY order_date
                 LIMIT 1,1) AS S
FROM Orders AS O;

# STEP 3
SELECT U.user_id AS seller_id,
       IF((SELECT item_brand FROM Items WHERE item_id = T.item_id) = U.favorite_brand,
          'yes', 'no') AS 2nd_item_fav_brand
FROM Users AS U
         LEFT JOIN
     (SELECT DISTINCT O1.seller_id,
                      (SELECT item_id
                       FROM Orders AS O2
                       WHERE O2.seller_id = O1.seller_id
                       ORDER BY order_date
                       LIMIT 1,1) AS item_id
      FROM Orders AS O1) AS T ON U.user_id = T.seller_id
         LEFT JOIN
     Items AS I ON T.item_id = I.item_id;