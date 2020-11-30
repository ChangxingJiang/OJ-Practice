Create table If Not Exists Activity
(
    user_id int,
    session_id int,
    activity_date date,
    activity_type ENUM ('open_session', 'end_session', 'scroll_down', 'send_message')
);

# # STEP 1
# SELECT COUNT(DISTINCT session_id)
# FROM Activity
# WHERE DATEDIFF('2020-07-27', activity_date) < 30
#   AND (activity_type = 'scroll_down' OR activity_type = 'send_message')
# GROUP BY user_id;
#
# # STEP 2
# SELECT ROUND(AVG(count), 2) AS average_sessions_per_user
# FROM (SELECT COUNT(DISTINCT session_id) AS count
#       FROM Activity
#       WHERE DATEDIFF('2020-07-27', activity_date) < 30
#         AND (activity_type = 'scroll_down' OR activity_type = 'send_message')
#       GROUP BY user_id) AS T;

SELECT IFNULL(ROUND(COUNT(DISTINCT session_id) / COUNT(DISTINCT user_id), 2), 0) AS average_sessions_per_user
FROM Activity
WHERE DATEDIFF('2019-07-27', activity_date) < 30;

