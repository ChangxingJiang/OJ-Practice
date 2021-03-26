Create table If Not Exists Users
(
    account int,
    name varchar(20)
);
Create table If Not Exists Transactions
(
    trans_id int,
    account int,
    amount int,
    transacted_on date
);

SELECT name,
       SUM(amount) AS balance
FROM Users
         LEFT JOIN
     Transactions USING (account)
GROUP BY account
HAVING balance > 10000;

