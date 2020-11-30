# LeetCode题解(1280)：学生们参加各科测试的次数(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/students-and-examinations/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 615ms (36.58%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
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
```