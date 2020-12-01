Create table If Not Exists SchoolA
(
    student_id int,
    student_name varchar(20)
);
Create table If Not Exists SchoolB
(
    student_id int,
    student_name varchar(20)
);
Create table If Not Exists SchoolC
(
    student_id int,
    student_name varchar(20)
);

SELECT S1.student_name AS member_A,
       S2.student_name AS member_B,
       S3.student_name AS member_C
FROM SchoolA AS S1,
     SchoolB AS S2,
     SchoolC AS S3
WHERE S1.student_id != s2.student_id
  AND S2.student_id != S3.student_id
  AND S1.student_id != S3.student_id
  AND S1.student_name != s2.student_name
  AND S2.student_name != S3.student_name
  AND S1.student_name != S3.student_name;