create table if not exists Transactions
(
    id int,
    country varchar(4),
    state enum ('approved', 'declined'),
    amount int,
    trans_date date
);

# STEP 1
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
       country,
       COUNT(id) AS approved_count,
       SUM(amount) AS approved_total_amount
FROM Transactions
WHERE state = 'approved'
GROUP BY country, DATE_FORMAT(trans_date, '%Y-%m');

# STEP 2
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month,
       country,
       COUNT(id) AS trans_count,
       SUM(amount) AS trans_total_amount
FROM Transactions
GROUP BY country, DATE_FORMAT(trans_date, '%Y-%m');

# STEP 3
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
