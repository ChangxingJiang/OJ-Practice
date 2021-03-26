Create table If Not Exists follow
(
    followee varchar(255),
    follower varchar(255)
);

SELECT followee AS follower,
       COUNT(DISTINCT follower) AS num
FROM follow
GROUP BY followee
HAVING followee IN (SELECT DISTINCT follower FROM follow)
ORDER BY followee;