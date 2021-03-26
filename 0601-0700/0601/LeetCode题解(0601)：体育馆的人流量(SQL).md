# LeetCode题解(0601)：体育馆的人流量(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/human-traffic-of-stadium/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 240ms (85.85%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT S3.id, S3.visit_date, S3.people
FROM stadium AS S3
         LEFT JOIN
     stadium AS S1 ON S1.id = S3.id - 2
         LEFT JOIN
     stadium AS S2 ON S2.id = S3.id - 1
         LEFT JOIN
     stadium AS S4 ON S4.id = S3.id + 1
         LEFT JOIN
     stadium AS S5 ON S5.id = S3.id + 2
WHERE S3.people >= 100
  AND ((S1.people >= 100 AND S2.people >= 100) OR
       (S2.people >= 100 AND S4.people >= 100) OR
       (S4.people >= 100 AND S5.people >= 100))
ORDER BY S3.id;
```