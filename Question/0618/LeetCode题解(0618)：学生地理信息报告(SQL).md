# LeetCode题解(0618)：学生地理信息报告(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/students-report-by-geography/)（困难）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 192ms (61.66%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT P1.name AS America,
       P2.name AS Asia,
       P3.name AS Europe
FROM (SELECT T1.id, T1.name
      FROM (SELECT @id1 := 0) AS ID1,
           (SELECT @id1 := @id1 + 1 AS id, name
            FROM student
            WHERE continent = 'America'
            ORDER BY name) AS T1) AS P1
         LEFT JOIN
     (SELECT T2.id, T2.name
      FROM (SELECT @id2 := 0) AS ID2,
           (SELECT @id2 := @id2 + 1 AS id, name
            FROM student
            WHERE continent = 'Asia'
            ORDER BY name) AS T2) AS P2 ON P2.id = P1.id
         LEFT JOIN
     (SELECT T3.id, T3.name
      FROM (SELECT @id3 := 0) AS ID3,
           (SELECT @id3 := @id3 + 1 AS id, name
            FROM student
            WHERE continent = 'Europe'
            ORDER BY name) AS T3) AS P3 ON P3.id = P1.id;
```