Create table If Not Exists Users
(
    user_id int,
    user_name varchar(20),
    credit int
);
Create table If Not Exists Transactions
(
    trans_id int,
    paid_by int,
    paid_to int,
    amount int,
    transacted_on date
);

# STEP 1
SELECT paid_by AS user_id,
       amount
FROM Transactions;

SELECT paid_to AS user_id,
       -amount AS amount
FROM Transactions;

# STEP 2
SELECT paid_by AS user_id,
       amount
FROM Transactions
UNION
SELECT paid_to AS user_id,
       -amount AS amount
FROM Transactions;

# STEP 3
SELECT user_id,
       user_name,
       credit + IFNULL(SUM(IF(U.user_id = T.paid_to, 1, -1) * T.amount), 0) AS credit,
       IF(credit + IFNULL(SUM(IF(U.user_id = T.paid_to, 1, -1) * T.amount), 0) >= 0, 'No',
          'Yes') AS credit_limit_breached
FROM Users AS U
         LEFT JOIN
     Transactions AS T ON U.user_id = T.paid_to OR U.user_id = T.paid_by
GROUP BY user_id;
