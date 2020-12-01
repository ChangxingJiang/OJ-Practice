# LeetCode题解(1341)：电影评分(SQL)

题目：[原题链接]()（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 716ms (90.07%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
(SELECT U.name AS results
       FROM Movie_Rating AS T
                LEFT JOIN
            Users U on T.user_id = U.user_id
       GROUP BY T.user_id
       ORDER BY COUNT(*) DESC, U.name
       LIMIT 1)
UNION
(SELECT M . title AS results
      FROM Movie_Rating AS T
      LEFT JOIN
      Movies AS M ON T . movie_id = M . movie_id
      where T . created_at BETWEEN '2020-02-01' AND '2020-02-29'
      GROUP BY T . movie_id
      ORDER BY AVG(rating) DESC, M.title
         LIMIT 1);
```