Create table If Not Exists Spending
(
    user_id int,
    spend_date date,
    platform ENUM ('desktop', 'mobile'),
    amount int
);

# STEP 1
SELECT user_id,
       spend_date,
       IF(COUNT(DISTINCT platform) = 1, platform, 'both') AS platform,
       SUM(amount) AS amount
FROM Spending
GROUP BY user_id, spend_date;

# STEP 2
SELECT spend_date,
       platform,
       SUM(amount) AS total_amount,
       COUNT(DISTINCT user_id) AS total_users
FROM (SELECT user_id,
             spend_date,
             IF(COUNT(DISTINCT platform) = 1, platform, 'both') AS platform,
             SUM(amount) AS amount
      FROM Spending
      GROUP BY user_id, spend_date) AS T
GROUP BY spend_date, platform;

# STEP 3
SELECT DISTINCT S.spend_date,
                P.platform,
                IFNULL(T.total_amount,0) AS total_amount,
                IFNULL(T.total_users,0) AS total_users
FROM Spending AS S
         CROSS JOIN
     (SELECT 'mobile' AS platform
      UNION
      SELECT 'desktop' AS platform
      UNION
      SELECT 'both' AS platform) AS P
         LEFT JOIN
     (SELECT spend_date,
             platform,
             SUM(amount) AS total_amount,
             COUNT(DISTINCT user_id) AS total_users
      FROM (SELECT user_id,
                   spend_date,
                   IF(COUNT(DISTINCT platform) = 1, platform, 'both') AS platform,
                   SUM(amount) AS amount
            FROM Spending
            GROUP BY user_id, spend_date) AS T
      GROUP BY spend_date, platform) AS T ON T.spend_date = S.spend_date AND T.platform = P.platform;
