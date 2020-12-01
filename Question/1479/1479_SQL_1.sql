Create table If Not Exists Orders
(
    order_id int,
    customer_id int,
    order_date date,
    item_id varchar(30),
    quantity int
);
Create table If Not Exists Items
(
    item_id varchar(30),
    item_name varchar(30),
    item_category varchar(30)
);

SELECT DISTINCT I.item_category AS Category,
                IFNULL(SUM(IF(DAYOFWEEK(O.order_date) = 2, O.quantity, 0)), 0) AS Monday,
                IFNULL(SUM(IF(DAYOFWEEK(O.order_date) = 3, O.quantity, 0)), 0) AS Tuesday,
                IFNULL(SUM(IF(DAYOFWEEK(O.order_date) = 4, O.quantity, 0)), 0) AS Wednesday,
                IFNULL(SUM(IF(DAYOFWEEK(O.order_date) = 5, O.quantity, 0)), 0) AS Thursday,
                IFNULL(SUM(IF(DAYOFWEEK(O.order_date) = 6, O.quantity, 0)), 0) AS Friday,
                IFNULL(SUM(IF(DAYOFWEEK(O.order_date) = 7, O.quantity, 0)), 0) AS Saturday,
                IFNULL(SUM(IF(DAYOFWEEK(O.order_date) = 1, O.quantity, 0)), 0) AS Sunday
FROM Orders AS O
         RIGHT JOIN
     Items AS I USING (item_id)
GROUP BY Category
ORDER BY Category;


