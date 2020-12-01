Create table If Not Exists Countries
(
    country_id int,
    country_name varchar(20)
);
Create table If Not Exists Weather
(
    country_id int,
    weather_state int,
    day date
);

# STEP 1
SELECT country_id,
       CASE
           WHEN AVG(weather_state) <= 15 THEN 'Cold'
           WHEN AVG(weather_state) >= 25 THEN 'Hot'
           ELSE 'Warm' END AS weather_type
FROM Weather
WHERE day BETWEEN '2019-11-01' AND '2019-11-30'
GROUP BY country_id;

# STEP 2
SELECT C.country_name,
       T.weather_type
FROM (SELECT country_id,
             CASE
                 WHEN AVG(weather_state) <= 15 THEN 'Cold'
                 WHEN AVG(weather_state) >= 25 THEN 'Hot'
                 ELSE 'Warm' END AS weather_type
      FROM Weather
      WHERE day BETWEEN '2019-11-01' AND '2019-11-30'
      GROUP BY country_id) AS T
         LEFT JOIN
     Countries AS C ON C.country_id = T.country_id;
