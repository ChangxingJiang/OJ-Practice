Create table If Not Exists seat
(
    id int,
    student varchar(255)
);

SELECT S1.id as id,
       IF(S1.id MOD 2 = 1, IFNULL(S2.student, S1.student), S3.student) as student
FROM seat AS S1
         LEFT JOIN
     seat AS S2 ON S2.id = S1.id + 1
         LEFT JOIN
     seat AS S3 ON S3.id = S1.id - 1;
