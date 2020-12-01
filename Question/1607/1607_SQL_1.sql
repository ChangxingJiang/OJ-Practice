Create table If Not Exists Customer
(
    customer_id int,
    customer_name varchar(20)
);
Create table If Not Exists Orders
(
    order_id int,
    sale_date date,
    order_cost int,
    customer_id int,
    seller_id int
);
Create table If Not Exists Seller
(
    seller_id int,
    seller_name varchar(20)
);

SELECT seller_name
FROM Seller
WHERE seller_id NOT IN (SELECT seller_id
                        FROM Orders
                        WHERE sale_date > '2020-01-01')
ORDER BY seller_name;
