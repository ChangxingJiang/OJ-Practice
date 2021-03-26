Create table If Not Exists Queue
(
    person_id int,
    person_name varchar(30),
    weight int,
    turn int
);

# STEP 1
SELECT person_name, @now := @now + weight AS weight
FROM Queue,
     (SELECT @now := 0) AS T
ORDER BY turn;

# STEP 2
SELECT person_name
FROM (SELECT person_name, @now := @now + weight AS weight
      FROM Queue,
           (SELECT @now := 0) AS T1
      ORDER BY turn
) AS T2
WHERE weight <= 1000
ORDER BY weight DESC
LIMIT 1;