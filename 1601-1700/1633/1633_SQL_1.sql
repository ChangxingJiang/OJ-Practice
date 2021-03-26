Create table If Not Exists Users
(
    user_id int,
    user_name varchar(20)
);
Create table If Not Exists Register
(
    contest_id int,
    user_id int
);

SELECT contest_id,
       ROUND(COUNT(DISTINCT user_id) / (SELECT COUNT(user_id) FROM Users) * 100, 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id;