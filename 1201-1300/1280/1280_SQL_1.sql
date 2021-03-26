Create table If Not Exists Students
(
    student_id int,
    student_name varchar(20)
);
Create table If Not Exists Subjects
(
    subject_name varchar(20)
);
Create table If Not Exists Examinations
(
    student_id int,
    subject_name varchar(20)
)

# Step 1
SELECT ST.student_id,
       ST.student_name,
       SU.subject_name
FROM Students AS ST
         CROSS JOIN
     Subjects AS SU;

# Step 2
SELECT student_id,
       subject_name,
       COUNT(*) AS attended_exams
FROM Examinations
GROUP BY student_id, subject_name;

# Step 3
SELECT ST.student_id,
       ST.student_name,
       SU.subject_name,
       IFnull(E.attended_exams, 0) AS attended_exams
FROM Students AS ST
         CROSS JOIN
     Subjects AS SU
         LEFT JOIN
     (SELECT student_id,
             subject_name,
             COUNT(*) AS attended_exams
      FROM Examinations
      GROUP BY student_id, subject_name) AS E
     ON E.student_id = ST.student_id AND E.subject_name = SU.subject_name
ORDER BY student_id, subject_name;

