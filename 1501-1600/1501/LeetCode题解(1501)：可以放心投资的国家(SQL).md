# LeetCode题解(1501)：可以放心投资的国家(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/countries-you-can-safely-invest-in/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 803ms (57.68%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT country
FROM (
         SELECT T2.country,
                duration
         FROM Calls AS T1
                  LEFT JOIN
              (SELECT P.id,
                      C.name AS country
               FROM Person AS P
                        JOIN
                    Country AS C ON LEFT(P.phone_number, 3) = C.country_code) AS T2 ON T1.callee_id = T2.id
         UNION ALL
         SELECT T2.country,
                duration
         FROM Calls AS T1
                  LEFT JOIN
              (SELECT P.id,
                      C.name AS country
               FROM Person AS P
                        JOIN
                    Country AS C ON LEFT(P.phone_number, 3) = C.country_code) AS T2 ON T1.caller_id = T2.id
     ) AS T
GROUP BY T.country
HAVING AVG(T.duration) > (SELECT AVG(duration) FROM Calls);
```