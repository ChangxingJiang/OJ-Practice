Create table If Not Exists Trips
(
    Id int,
    Client_Id int,
    Driver_Id int,
    City_Id int,
    Status ENUM ('completed', 'cancelled_by_driver', 'cancelled_by_client'),
    Request_at varchar(50)
);
Create table If Not Exists Users
(
    Users_Id int,
    Banned varchar(50),
    Role ENUM ('client', 'driver', 'partner')
);

SELECT T.Request_at AS `Day`,
       ROUND(SUM(IF(T.Status = 'completed', 0, 1)) / COUNT(T.Status), 2) AS `Cancellation Rate`
FROM Trips AS T
WHERE T.Client_Id NOT IN (
    SELECT Users_Id
    FROM Users
    WHERE Banned = 'Yes'
)
  AND T.Driver_Id NOT IN (
    SELECT Users_Id
    FROM Users
    WHERE Banned = 'Yes'
)
  AND T.Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY T.Request_at;


