Create table If Not Exists student
(
    name varchar(50),
    continent varchar(7)
);

# STEP 1
SELECT T1.id, T1.name
FROM (SELECT @id1 := 0) AS ID1,
     (SELECT @id1 := @id1 + 1 AS id, name
      FROM student
      WHERE continent = 'America'
      ORDER BY name) AS T1;

# STEP 2
SELECT T2.id, T2.name
FROM (SELECT @id2 := 0) AS ID2,
     (SELECT @id2 := @id2 + 1 AS id, name
      FROM student
      WHERE continent = 'Asia'
      ORDER BY name) AS T2;

# STEP 3
SELECT T3.id, T3.name
FROM (SELECT @id3 := 0) AS ID3,
     (SELECT @id3 := @id3 + 1 AS id, name
      FROM student
      WHERE continent = 'Asia'
      ORDER BY name) AS T3;

# STEP 4
SELECT P1.name AS America,
       P2.name AS Asia,
       P3.name AS Europe
FROM (SELECT T1.id, T1.name
      FROM (SELECT @id1 := 0) AS ID1,
           (SELECT @id1 := @id1 + 1 AS id, name
            FROM student
            WHERE continent = 'America'
            ORDER BY name) AS T1) AS P1
         LEFT JOIN
     (SELECT T2.id, T2.name
      FROM (SELECT @id2 := 0) AS ID2,
           (SELECT @id2 := @id2 + 1 AS id, name
            FROM student
            WHERE continent = 'Asia'
            ORDER BY name) AS T2) AS P2 ON P2.id = P1.id
         LEFT JOIN
     (SELECT T3.id, T3.name
      FROM (SELECT @id3 := 0) AS ID3,
           (SELECT @id3 := @id3 + 1 AS id, name
            FROM student
            WHERE continent = 'Europe'
            ORDER BY name) AS T3) AS P3 ON P3.id = P1.id;