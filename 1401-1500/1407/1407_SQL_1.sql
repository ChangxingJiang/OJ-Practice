Create Table If Not Exists Users
(
    id int,
    name varchar(30)
);
Create Table If Not Exists Rides
(
    id int,
    user_id int,
    distance int
);

SELECT U.name,
       IFNULL(SUM(distance),0) AS travelled_distance
FROM Users U
         LEFT JOIN
     Rides AS R ON R.user_id = U.id
GROUP BY user_id
ORDER BY travelled_distance DESC, U.name;
