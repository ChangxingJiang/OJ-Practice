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

# 生成月份列表
WITH RECURSIVE A AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1
    FROM A
    WHERE month < 10
)

# 查询每月的值
SELECT MONTH(requested_at) AS month,
       IFNULL(SUM(ride_distance), 0) AS sum_ride_distance,
       IFNULL(SUM(ride_duration), 0) AS sum_ride_duration
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
    WHERE month < 10
)
SELECT L.month,
       ROUND(IFNULL(SUM(ride_distance) / 3, 0), 2) AS average_ride_distance,
       ROUND(IFNULL(SUM(ride_duration) / 3, 0), 2) AS average_ride_duration
FROM MonthList AS L
         LEFT JOIN
     (
         SELECT *
         FROM Rides AS R
                  LEFT JOIN
              AcceptedRides USING (ride_id)
         WHERE YEAR(requested_at) = 2020
     ) AS T ON L.month - MONTH(requested_at) BETWEEN -2 AND 0
GROUP BY month
ORDER BY month;

