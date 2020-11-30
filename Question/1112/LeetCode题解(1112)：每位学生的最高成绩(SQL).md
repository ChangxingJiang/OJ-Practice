# LeetCode题解(1112)：每位学生的最高成绩(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/highest-grade-for-each-student/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 429ms (32.02%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
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
```