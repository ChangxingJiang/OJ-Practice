Create table If Not Exists Visits
(
    user_id int,
    visit_date date
);
Create table If Not Exists Transactions
(
    user_id int,
    transaction_date date,
    amount int
);

SELECT user_id, visit_date
FROM Visits;

SELECT user_id, transaction_date, COUNT(amount) AS count
FROM Transactions
GROUP BY user_id, transaction_date;

SELECT V.user_id,
       V.visit_date,
       IFNULL(T.count, 0) AS count
FROM Visits AS V
         LEFT JOIN
     (SELECT user_id, transaction_date, COUNT(amount) AS count
      FROM Transactions
      GROUP BY user_id, transaction_date) AS T ON V.user_id = T.user_id AND
                                                  V.visit_date = T.transaction_date;

SELECT count AS transactions_count,
       COUNT(*) AS visits_count
FROM (SELECT V.user_id,
             V.visit_date,
             IFNULL(T.count, 0) AS count
      FROM Visits AS V
               LEFT JOIN
           (SELECT user_id, transaction_date, COUNT(amount) AS count
            FROM Transactions
            GROUP BY user_id, transaction_date) AS T ON V.user_id = T.user_id AND
                                                        V.visit_date = T.transaction_date) AS S
GROUP BY count
ORDER BY count;

SELECT @min_idx := MIN(transactions_count), @max_idx := MAX(transactions_count)
FROM (SELECT count AS transactions_count
      FROM (SELECT IFNULL(T.count, 0) AS count
            FROM Visits AS V
                     LEFT JOIN
                 (SELECT user_id, transaction_date, COUNT(amount) AS count
                  FROM Transactions
                  GROUP BY user_id, transaction_date) AS T ON V.user_id = T.user_id AND
                                                              V.visit_date = T.transaction_date) AS S1
      GROUP BY count
      ORDER BY count) AS S2;

SELECT @id := @id + 1 AS transactions_count,
       @min_idx,
       @max_idx
FROM (SELECT @min_idx := MIN(transactions_count), @max_idx := MAX(transactions_count)
      FROM (SELECT count AS transactions_count
            FROM (SELECT IFNULL(T.count, 0) AS count
                  FROM Visits AS V
                           LEFT JOIN
                       (SELECT user_id, transaction_date, COUNT(amount) AS count
                        FROM Transactions
                        GROUP BY user_id, transaction_date) AS T ON V.user_id = T.user_id AND
                                                                    V.visit_date = T.transaction_date) AS S1
            GROUP BY count
            ORDER BY count) AS S2) AS O1,
     (SELECT @id := @min_idx - 1) AS O2
WHERE @id <= @max_idx;

SELECT 0 AS transactions_count,
       COUNT(*) AS visits_count
FROM (
         SELECT user_id, visit_date
         FROM Visits
         WHERE (user_id, visit_date) NOT IN
               (SELECT user_id, transaction_date FROM Transactions)
     ) AS T1
UNION ALL
SELECT T2.id AS transactions_count,
       IFNULL(T3.visits_count, 0) AS visits_count
FROM (
         SELECT id
         FROM (SELECT (@x := @x + 1) AS id
               FROM Transactions,
                    (SELECT @x := 0) AS ID) AS T4
         WHERE id <= (
             SELECT max(transactions_count)
             FROM (
                      SELECT count(*) AS transactions_count
                      FROM Transactions
                      GROUP BY user_id, transaction_date
                  ) AS T5
         )
     ) T2
         LEFT JOIN
     (
         SELECT transactions_count,
                COUNT(transactions_count) AS visits_count
         FROM (
                  SELECT count(*) AS transactions_count
                  FROM Transactions
                  GROUP BY user_id, transaction_date
              ) AS T6
         GROUP BY transactions_count
     ) T3
     ON T2.id = T3.transactions_count
ORDER BY transactions_count;
