Create table If Not Exists Delivery
(
    delivery_id int,
    customer_id int,
    order_date date,
    customer_pref_delivery_date date
);

# STEP 1
SELECT delivery_id, True AS immediate
FROM Delivery
WHERE order_date = customer_pref_delivery_date;

# STEP2
SELECT delivery_id, MIN(order_date)
FROM Delivery
GROUP BY delivery_id;

# STEP 3
SELECT ROUND(SUM(IFNULL(T.immediate, 0)) / COUNT(D.delivery_id) * 100, 2) AS immediate_percentage
FROM Delivery AS D
         LEFT JOIN
     (SELECT delivery_id, 1 AS immediate
      FROM Delivery
      WHERE order_date = customer_pref_delivery_date) AS T ON D.delivery_id = T.delivery_id
WHERE (D.customer_id, D.order_date) IN (SELECT customer_id, MIN(order_date)
                                        FROM Delivery
                                        GROUP BY customer_id);