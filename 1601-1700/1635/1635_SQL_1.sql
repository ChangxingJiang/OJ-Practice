Create table If Not Exists Drivers
(
    driver_id int,
    join_date date
);
Create table If Not Exists Rides
(
    ride_id int,
    user_id int,
    requested_at date
);
Create table If Not Exists AcceptedRides
(
    ride_id int,
    driver_id int,
    ride_distance int,
    ride_duration int
);

# 每月活跃车手数量
SELECT DATE_FORMAT(join_date, '%Y-%m') AS month,
       @now := @now + 1 AS active_driver
FROM Drivers,
     (SELECT @now := 0) AS T1
ORDER BY join_date;

SELECT MONTH(join_date) AS month,
       MAX(active_driver) AS active_driver
FROM (SELECT join_date,
             @now := @now + 1 AS active_driver
      FROM Drivers,
           (SELECT @now := 0) AS T1
      ORDER BY join_date) AS T2
WHERE YEAR(join_date) = 2020
GROUP BY month;

# 生成月份列表
WITH RECURSIVE A AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1
    FROM A
    WHERE month < 12
)

# 计算每月的接收情况
SELECT MONTH(requested_at) AS month,
       SUM(AR.ride_id IS NOT NULL) AS accepted_rides
FROM Rides AS R
         LEFT JOIN
     AcceptedRides AS AR on R.ride_id = AR.ride_id
WHERE requested_at BETWEEN '2020-01-01' AND '2020-12-31'
GROUP BY MONTH(requested_at);

# 最终结果
WITH RECURSIVE MonthList AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1
    FROM MonthList
    WHERE month < 12
)
SELECT L.month,
       CONVERT(IF(D.month IS NOT NULL, @last := active_driver, @last), DECIMAL) AS active_drivers,
       IFNULL(A.accepted_rides, 0) AS accepted_rides
FROM MonthList AS L
         LEFT JOIN
     (
         SELECT MONTH(join_date) AS month,
                MAX(active_driver) AS active_driver
         FROM (SELECT join_date,
                      @now := @now + 1 AS active_driver
               FROM Drivers,
                    (SELECT @now := 0) AS T1
               ORDER BY join_date) AS T2
         WHERE YEAR(join_date) = 2020
         GROUP BY month
     ) AS D ON L.month = D.month
         LEFT JOIN
     (
         SELECT MONTH(requested_at) AS month,
                SUM(AR.ride_id IS NOT NULL) AS accepted_rides
         FROM Rides AS R
                  LEFT JOIN
              AcceptedRides AS AR on R.ride_id = AR.ride_id
         WHERE requested_at BETWEEN '2020-01-01' AND '2020-12-31'
         GROUP BY MONTH(requested_at)
     ) AS A ON L.month = A.month,
     (SELECT @last := 0) AS T3;



