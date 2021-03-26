Create table If Not Exists Failed
(
    fail_date date
);
Create table If Not Exists Succeeded
(
    success_date date
);

# Step 1
SELECT success_date AS date,
       IF(DATEDIFF(@pre_date, @pre_date := success_date) = -1, @id, @id := @id + 1) AS id
FROM Succeeded,
     (SELECT @id := 0, @pre_date := NULL) AS Param;

# Step 2
SELECT MIN(T1.date) AS start_date,
       MAX(T1.date) AS end_date
FROM (SELECT success_date AS date,
             IF(DATEDIFF(@pre_date, @pre_date := success_date) = -1, @id, @id := @id + 1) AS id
      FROM Succeeded,
           (SELECT @id := 0, @pre_date := NULL) AS Param) AS T1
GROUP BY T1.id;

# Step 3
SELECT MIN(T2.date) AS start_date,
       MAX(T2.date) AS end_date
FROM (SELECT fail_date AS date,
             IF(DATEDIFF(@pre_date, @pre_date := fail_date) = -1, @id, @id := @id + 1) AS id
      FROM Failed,
           (SELECT @id := 0, @pre_date := NULL) AS Param) AS T2
GROUP BY T2.id;

# Step 4
SELECT period_state,
       MIN(T1.date) AS start_date,
       MAX(T1.date) AS end_date
FROM (SELECT success_date AS date,
             'succeeded' AS period_state,
             IF(DATEDIFF(@pre_date, @pre_date := success_date) = -1, @id, @id := @id + 1) AS id
      FROM Succeeded,
           (SELECT @id := 0, @pre_date := NULL) AS Param) AS T1
GROUP BY T1.id;

SELECT period_state,
       MIN(T2.date) AS start_date,
       MAX(T2.date) AS end_date
FROM (SELECT fail_date AS date,
             'failed' AS period_state,
             IF(DATEDIFF(@pre_date, @pre_date := fail_date) = -1, @id, @id := @id + 1) AS id
      FROM Failed,
           (SELECT @id := 0, @pre_date := NULL) AS Param) AS T2
GROUP BY T2.id;

# Step 5
SELECT period_state,
       MIN(T.date) AS start_date,
       MAX(T.date) AS end_date
FROM (SELECT success_date AS date,
             'succeeded' AS period_state,
             IF(DATEDIFF(@pre_date, @pre_date := success_date) = -1, @id, @id := @id + 1) AS id
      FROM Succeeded,
           (SELECT @id := 0, @pre_date := NULL) AS Param
      UNION
      SELECT fail_date AS date,
             'failed' AS period_state,
             IF(DATEDIFF(@pre_date, @pre_date := fail_date) = -1, @id, @id := @id + 1) AS id
      FROM Failed,
           (SELECT @id := 0, @pre_date := NULL) AS Param
     ) AS T
WHERE date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY T.id
ORDER BY start_date;

