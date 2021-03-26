# LeetCode题解(0580)：统计各专业学生人数(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/count-student-number-in-departments/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 626ms (25.86%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT D.dept_name AS dept_name,
       IFNULL(S.student_number, 0) AS student_number
FROM department AS D
         LEFT JOIN
     (SELECT dept_id,
             COUNT(*) AS student_number
      FROM student
      GROUP BY dept_id) AS S ON D.dept_id = S.dept_id
ORDER BY student_number DESC, dept_name;
```