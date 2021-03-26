Create table If Not Exists Users
(
    user_id int,
    name varchar(40)
);

SELECT user_id,
       CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id;
