Create table If Not Exists Actions
(
    user_id int,
    post_id int,
    action_date date,
    action ENUM ('view', 'like', 'reaction', 'comment', 'report', 'share'),
    extra varchar(10)
);
create table if not exists Removals
(
    post_id int,
    remove_date date
);

# STEP 1
SELECT COUNT(DISTINCT R.post_id) / COUNT(DISTINCT A.post_id) * 100 AS rate
FROM Actions AS A
         LEFT JOIN
     Removals AS R on A.post_id = R.post_id
WHERE A.action = 'report'
  AND A.extra = 'spam'
GROUP BY action_date;

# STEP 2
SELECT ROUND(AVG(rate), 2) AS average_daily_percent
FROM (SELECT COUNT(DISTINCT R.post_id) / COUNT(DISTINCT A.post_id) * 100 AS rate
      FROM Actions AS A
               LEFT JOIN
           Removals AS R on A.post_id = R.post_id
      WHERE A.action = 'report'
        AND A.extra = 'spam'
      GROUP BY action_date) AS T;
