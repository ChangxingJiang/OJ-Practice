Create table If Not Exists Friends
(
    id int,
    name varchar(30),
    activity varchar(30)
);
Create table If Not Exists Activities
(
    id int,
    name varchar(30)
);

SELECT activity,
       COUNT(*) AS count
FROM Friends
GROUP BY activity;

SELECT name AS activity
FROM Activities AS A
         LEFT JOIN
     (SELECT activity,
             COUNT(*) AS count
      FROM Friends
      GROUP BY activity) AS F ON A.name = F.activity
WHERE IFNULL(F.count, 0) != (SELECT IFNULL(count, 0)
                             FROM Activities AS A
                                      LEFT JOIN
                                  (SELECT activity,
                                          COUNT(*) AS count
                                   FROM Friends
                                   GROUP BY activity) AS F ON A.name = F.activity
                             ORDER BY count
                             LIMIT 1)
  AND IFNULL(F.count, 0) != (SELECT IFNULL(count, 0)
                             FROM Activities AS A
                                      LEFT JOIN
                                  (SELECT activity,
                                          COUNT(*) AS count
                                   FROM Friends
                                   GROUP BY activity) AS F ON A.name = F.activity
                             ORDER BY count DESC
                             LIMIT 1);
