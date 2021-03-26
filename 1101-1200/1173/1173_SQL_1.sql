Create table If Not Exists Delivery
(
    delivery_id int,
    customer_id int,
    order_date date,
    customer_pref_delivery_date date
);

# STEP 1
SELECT delivery_id
FROM Delivery
WHERE order_date = customer_pref_delivery_date;

# STEP 2
SELECT ROUND((SELECT COUNT(delivery_id)
              FROM Delivery
              WHERE order_date = customer_pref_delivery_date)
                 /
             (SELECT COUNT(delivery_id)
              FROM Delivery)
                 * 100
           , 2) AS immediate_percentage;