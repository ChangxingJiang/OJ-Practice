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