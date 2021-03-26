Create table If Not Exists UserActivity
(
    username varchar(30),
    activity varchar(30),
    startDate date,
    endDate date
);

SELECT username, max(startDate)
FROM UserActivity
GROUP BY username
HAVING COUNT(username) > 1;

SELECT username, max(startDate)
FROM UserActivity
WHERE (username, startDate) NOT IN (SELECT username, max(startDate)
                                    FROM UserActivity
                                    GROUP BY username
                                    HAVING COUNT(username) > 1)
GROUP BY username;

SELECT username, activity, startDate, endDate
FROM UserActivity
WHERE (username, startDate) IN (SELECT username, max(startDate)
                                FROM UserActivity
                                WHERE (username, startDate) NOT IN (SELECT username, max(startDate)
                                                                    FROM UserActivity
                                                                    GROUP BY username
                                                                    HAVING COUNT(username) > 1)
                                GROUP BY username);