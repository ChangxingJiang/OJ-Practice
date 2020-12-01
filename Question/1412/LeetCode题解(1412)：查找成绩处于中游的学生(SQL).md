# LeetCode题解(1412)：查找成绩处于中游的学生(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-quiet-students-in-all-exams/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 399ms (46.46%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
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
```