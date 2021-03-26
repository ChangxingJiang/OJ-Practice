Create table If Not Exists Person
(
    id int,
    name varchar(15),
    phone_number varchar(11)
);
Create table If Not Exists Country
(
    name varchar(15),
    country_code varchar(3)
);
Create table If Not Exists Calls
(
    caller_id int,
    callee_id int,
    duration int
);

SELECT P.id,
       C.name AS country
FROM Person AS P
         JOIN
     Country AS C ON LEFT(P.phone_number, 3) = C.country_code;

SELECT T2.country,
       duration
FROM Calls AS T1
         LEFT JOIN
     (SELECT P.id,
             C.name AS country
      FROM Person AS P
               JOIN
           Country AS C ON LEFT(P.phone_number, 3) = C.country_code) AS T2 ON T1.callee_id = T2.id;

SELECT T2.country,
       duration
FROM Calls AS T1
         LEFT JOIN
     (SELECT P.id,
             C.name AS country
      FROM Person AS P
               JOIN
           Country AS C ON LEFT(P.phone_number, 3) = C.country_code) AS T2 ON T1.caller_id = T2.id;

SELECT country
FROM (
         SELECT T2.country,
                duration
         FROM Calls AS T1
                  LEFT JOIN
              (SELECT P.id,
                      C.name AS country
               FROM Person AS P
                        JOIN
                    Country AS C ON LEFT(P.phone_number, 3) = C.country_code) AS T2 ON T1.callee_id = T2.id
         UNION ALL
         SELECT T2.country,
                duration
         FROM Calls AS T1
                  LEFT JOIN
              (SELECT P.id,
                      C.name AS country
               FROM Person AS P
                        JOIN
                    Country AS C ON LEFT(P.phone_number, 3) = C.country_code) AS T2 ON T1.caller_id = T2.id
     ) AS T
GROUP BY T.country
HAVING AVG(T.duration) > (SELECT AVG(duration) FROM Calls);

# SELECT country
# FROM (SELECT country,
#              SUM(duration) AS duration
#       FROM (
#                SELECT T2.country,
#                       duration
#                FROM Calls AS T1
#                         LEFT JOIN
#                     (SELECT P.id,
#                             C.name AS country
#                      FROM Person AS P
#                               JOIN
#                           Country AS C ON LEFT(P.phone_number, 3) = C.country_code) AS T2 ON T1.callee_id = T2.id
#                UNION ALL
#                SELECT T2.country,
#                       duration
#                FROM Calls AS T1
#                         LEFT JOIN
#                     (SELECT P.id,
#                             C.name AS country
#                      FROM Person AS P
#                               JOIN
#                           Country AS C ON LEFT(P.phone_number, 3) = C.country_code) AS T2 ON T1.caller_id = T2.id
#            ) AS T
#       GROUP BY T.country) AS O
# WHERE duration >
#       (SELECT AVG(duration)
#        FROM (SELECT duration
#              FROM (SELECT SUM(duration) AS duration
#                    FROM (
#                             SELECT T2.country,
#                                    duration
#                             FROM Calls AS T1
#                                      LEFT JOIN
#                                  (SELECT P.id,
#                                          C.name AS country
#                                   FROM Person AS P
#                                            JOIN
#                                        Country AS C ON LEFT(P.phone_number, 3) = C.country_code) AS T2
#                                  ON T1.callee_id = T2.id
#                             UNION ALL
#                             SELECT T2.country,
#                                    duration
#                             FROM Calls AS T1
#                                      LEFT JOIN
#                                  (SELECT P.id,
#                                          C.name AS country
#                                   FROM Person AS P
#                                            JOIN
#                                        Country AS C ON LEFT(P.phone_number, 3) = C.country_code) AS T2
#                                  ON T1.caller_id = T2.id
#                         ) AS T
#                    GROUP BY T.country) AS O1) AS O2);




