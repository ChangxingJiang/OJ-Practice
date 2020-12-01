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

# 计算每个月工作的车手数量
SELECT MONTH(requested_at) AS month,
       COUNT(DISTINCT driver_id) AS working_driver
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
       IFNULL(ROUND(O2.working_driver
                        /
                    IF(O1.month IS NOT NULL, @last := O1.active_driver, @last)
                        * 100
                  , 2), 0) AS working_percentage
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
     ) AS O1 ON L.month = O1.month
         LEFT JOIN
     (
         SELECT MONTH(requested_at) AS month,
                COUNT(DISTINCT driver_id) AS working_driver
         FROM Rides AS R
                  LEFT JOIN
              AcceptedRides AS AR on R.ride_id = AR.ride_id
         WHERE requested_at BETWEEN '2020-01-01' AND '2020-12-31'
         GROUP BY MONTH(requested_at)
     ) AS O2 ON L.month = O2.month,
     (SELECT @last := 0) AS T3;