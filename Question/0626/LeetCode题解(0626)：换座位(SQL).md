# LeetCode题解(0626)：换座位(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/exchange-seats/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 226ms (65.89%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT S1.id as id,
       IF(S1.id MOD 2 = 1, IFNULL(S2.student, S1.student), S3.student) as student
FROM seat AS S1
         LEFT JOIN
     seat AS S2 ON S2.id = S1.id + 1
         LEFT JOIN
     seat AS S3 ON S3.id = S1.id - 1;
```