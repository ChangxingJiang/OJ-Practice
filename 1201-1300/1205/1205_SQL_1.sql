create table if not exists Transactions
(
    id int,
    country varchar(4),
    state enum ('approved', 'declined'),
    amount int,
    trans_date date
);
create table if not exists Chargebacks
(
    trans_id int,
    trans_date date
);

# Before
SELECT T1.month,
       T1.country,
       T1.trans_count,
       IFNULL(T2.approved_count, 0) AS approved_count,
       T1.trans_total_amount,
       IFNULL(T2.approved_total_amount, 0) AS approved_total_amount
FROM (SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
             country,
             COUNT(id) AS trans_count,
             SUM(amount) AS trans_total_amount
      FROM Transactions
      GROUP BY country, DATE_FORMAT(trans_date, '%Y-%m')) AS T1
         LEFT JOIN
     (SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
             country,
             COUNT(id) AS approved_count,
             SUM(amount) AS approved_total_amount
      FROM Transactions
      WHERE state = 'approved'
      GROUP BY country, DATE_FORMAT(trans_date, '%Y-%m')) AS T2
     ON T1.month = T2.month AND T1.country = T2.country;

# Step 1
SELECT DATE_FORMAT(C.trans_date, '%Y-%m') AS month,
       TT.country,
       COUNT(TT.id) AS chargeback_count,
       SUM(TT.amount) AS chargeback_amount
FROM Chargebacks AS C
         LEFT JOIN
     (SELECT id, country, amount
      FROM Transactions) AS TT ON C.trans_id = TT.id
GROUP BY TT.country, DATE_FORMAT(C.trans_date, '%Y-%m');

# STEP 2
SELECT T.month,
       T.country,
       MAX(T.approved_count) AS approved_count,
       MAX(T.approved_amount) AS approved_amount,
       MAX(T.chargeback_count) AS chargeback_count,
       MAX(T.chargeback_amount) AS chargeback_amount
FROM (SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
             country,
             COUNT(id) AS approved_count,
             SUM(amount) AS approved_amount,
             0 AS chargeback_count,
             0 AS chargeback_amount
      FROM Transactions
      WHERE state = 'approved'
      GROUP BY country, DATE_FORMAT(trans_date, '%Y-%m')

      UNION

      SELECT DATE_FORMAT(C.trans_date, '%Y-%m') AS month,
             TT.country,
             0 AS approved_count,
             0 AS approved_amount,
             COUNT(TT.id) AS chargeback_count,
             SUM(TT.amount) AS chargeback_amount
      FROM Chargebacks AS C
               LEFT JOIN
           (SELECT id, country, amount
            FROM Transactions) AS TT ON C.trans_id = TT.id
      GROUP BY TT.country, DATE_FORMAT(C.trans_date, '%Y-%m')) AS T
GROUP BY T.country, T.month;