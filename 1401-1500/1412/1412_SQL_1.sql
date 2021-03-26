Create table If Not Exists Student
(
    student_id int,
    student_name varchar(30)
);
Create table If Not Exists Exam
(
    exam_id int,
    student_id int,
    score int
);

SELECT exam_id,
       MIN(score) AS min_score,
       MAX(score) AS max_score
FROM Exam
GROUP BY exam_id;

SELECT DISTINCT student_id
FROM Exam AS E1
         LEFT JOIN
     (SELECT exam_id,
             MIN(score) AS min_score,
             MAX(score) AS max_score
      FROM Exam
      GROUP BY exam_id) AS E2 ON E2.exam_id = E1.exam_id
WHERE E1.score = E2.min_score
   OR E1.score = E2.max_score;

SELECT student_id,
       student_name
FROM Student
WHERE student_id NOT IN (SELECT DISTINCT student_id
                         FROM Exam AS E1
                                  LEFT JOIN
                              (SELECT exam_id,
                                      MIN(score) AS min_score,
                                      MAX(score) AS max_score
                               FROM Exam
                               GROUP BY exam_id) AS E2 ON E2.exam_id = E1.exam_id
                         WHERE E1.score = E2.min_score
                            OR E1.score = E2.max_score)
  AND student_id IN (SELECT DISTINCT student_id FROM Exam);
