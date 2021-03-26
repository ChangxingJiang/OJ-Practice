Create table If Not Exists Logs
(
    log_id int
);

SELECT MIN(T.log_id) AS start_id,
       MAX(T.log_id) AS end_id
FROM (SELECT log_id,
             IF(@pre_date - (@pre_date := log_id) = -1, @id, @id := @id + 1) AS id
      FROM Logs,
           (SELECT @id := 0, @pre_date := NULL) AS Param) AS T
GROUP BY T.id;