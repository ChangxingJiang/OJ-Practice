CREATE TABLE IF NOT EXISTS student
(
    student_id INT,
    student_name VARCHAR(45),
    gender VARCHAR(6),
    dept_id INT
);
CREATE TABLE IF NOT EXISTS department
(
    dept_id INT,
    dept_name VARCHAR(255)
);

# Step 1
SELECT dept_id,
       COUNT(*) AS student_number
FROM student
GROUP BY dept_id;

# Step2
SELECT D.dept_name AS dept_name,
       IFNULL(S.student_number, 0) AS student_number
FROM department AS D
         LEFT JOIN
     (SELECT dept_id,
             COUNT(*) AS student_number
      FROM student
      GROUP BY dept_id) AS S ON D.dept_id = S.dept_id
ORDER BY student_number DESC, dept_name;
