Create table If Not Exists stadium
(
    id int,
    visit_date DATE NULL,
    people int
);

# STEP 1
SELECT S1.id, S1.visit_date, S1.people
FROM stadium AS S1
         LEFT JOIN
     stadium AS S2 ON S2.id = S1.id - 1
         LEFT JOIN
     stadium AS S3 ON S3.id = S1.id - 2
WHERE S1.people >= 100
  AND S2.people >= 100
  AND S3.people >= 100
ORDER BY S1.id;

# STEP 2
SELECT S3.id, S3.visit_date, S3.people
FROM stadium AS S3
         LEFT JOIN
     stadium AS S1 ON S1.id = S3.id - 2
         LEFT JOIN
     stadium AS S2 ON S2.id = S3.id - 1
         LEFT JOIN
     stadium AS S4 ON S4.id = S3.id + 1
         LEFT JOIN
     stadium AS S5 ON S5.id = S3.id + 2
WHERE S3.people >= 100
  AND ((S1.people >= 100 AND S2.people >= 100) OR
       (S2.people >= 100 AND S4.people >= 100) OR
       (S4.people >= 100 AND S5.people >= 100))
ORDER BY S3.id;