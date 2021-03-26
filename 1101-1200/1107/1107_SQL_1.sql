Create table If Not Exists Traffic
(
    user_id int,
    activity ENUM ('login', 'logout', 'jobs', 'groups', 'homepage'),
    activity_date date
);

# STEP 1
SELECT user_id, MIN(activity_date) AS login_date
FROM Traffic
WHERE activity = 'login'
GROUP BY user_id;

# STEP 2
SELECT login_date, COUNT(user_id) AS user_count
FROM (SELECT user_id, MIN(activity_date) AS login_date
      FROM Traffic
      WHERE activity = 'login'
      GROUP BY user_id) AS T
WHERE DATEDIFF('2019-06-30',login_date) <= 90
GROUP BY login_date;