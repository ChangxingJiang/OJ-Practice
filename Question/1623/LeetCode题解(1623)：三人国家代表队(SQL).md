# LeetCode题解(1623)：三人国家代表队(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/all-valid-triplets-that-can-represent-a-country/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) |            |            | 1773ms (31.93%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```mysql
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
```