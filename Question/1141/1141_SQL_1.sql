Create table If Not Exists Activity
(
    user_id int,
    session_id int,
    activity_date date,
    activity_type ENUM ('open_session', 'end_session', 'scroll_down', 'send_message')
);

SELECT activity_date AS day,
       COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE DATEDIFF('2019-07-27', activity_date) < 30
GROUP BY activity_date
HAVING active_users > 0;