Create table If Not Exists Users
(
    user_id int,
    name varchar(30),
    mail varchar(50)
);

SELECT *
FROM Users
WHERE mail REGEXP '^[a-zA-Z]+[\\w/.\\-]*(@leetcode.com)$';