Create table If Not Exists Events
(
    business_id int,
    event_type varchar(10),
    occurences int
);

# STEP 1
SELECT event_type, AVG(occurences) AS occurences
FROM Events
GROUP BY event_type;

# STEP 2
SELECT E.business_id
FROM Events AS E
         LEFT JOIN
     (SELECT event_type, AVG(occurences) AS occurences
      FROM Events
      GROUP BY event_type) AS AVG ON E.event_type = AVG.event_type
WHERE E.occurences > AVG.occurences
GROUP BY E.business_id
HAVING COUNT(*) >=2;

# STEP 3
SELECT business_id, SUM(occurences) AS occurences
FROM (SELECT @avg := SUM(occurences) / COUNT(DISTINCT business_id) FROM Events) AS E,
     Events
GROUP BY business_id
HAVING SUM(occurences) > @avg;


