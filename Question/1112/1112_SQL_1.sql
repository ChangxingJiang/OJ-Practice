Create table If Not Exists Enrollments
(
    student_id int,
    course_id int,
    grade int
);

# STEP 1
SELECT student_id, MAX(grade) AS max_grade
FROM Enrollments
GROUP BY student_id;

#STEP 2
SELECT E.student_id, MIN(course_id) AS min_course
FROM Enrollments AS E
         LEFT JOIN
     (SELECT student_id, MAX(grade) AS max_grade
      FROM Enrollments
      GROUP BY student_id) AS T ON E.student_id = T.student_id
WHERE grade = max_grade
GROUP BY T.student_id;

# STEP 3
SELECT E.student_id, E.course_id, E.grade
FROM Enrollments AS E
         LEFT JOIN
     (SELECT E.student_id, MIN(course_id) AS min_course
      FROM Enrollments AS E
               LEFT JOIN
           (SELECT student_id, MAX(grade) AS max_grade
            FROM Enrollments
            GROUP BY student_id) AS T1 ON E.student_id = T1.student_id
      WHERE grade = max_grade
      GROUP BY T1.student_id) AS T2 ON E.student_id = T2.student_id
WHERE E.course_id = min_course
ORDER BY E.student_id;