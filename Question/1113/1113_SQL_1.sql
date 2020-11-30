Create table If Not Exists Actions
(
    user_id int,
    post_id int,
    action_date date,
    action ENUM ('view', 'like', 'reaction', 'comment', 'report', 'share'),
    extra varchar(10)
);

SELECT extra AS report_reason,
       COUNT(DISTINCT post_id) AS report_count
FROM Actions
WHERE DATEDIFF('2019-07-05', action_date) = 1
  AND action = 'report'
GROUP BY extra;