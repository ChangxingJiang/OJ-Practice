Create table If Not Exists Visits
(
    visit_id int,
    customer_id int
);
Create table If Not Exists Transactions
(
    transaction_id int,
    visit_id int,
    amount int
);

SELECT customer_id,
       COUNT(DISTINCT visit_id) AS count_no_trans
FROM Visits
WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)
GROUP BY customer_id;


