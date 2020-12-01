# LeetCode题解(1241)：每个帖子的评论数(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-comments-per-post/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 965ms (71.55%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT T1.post_id,
       IFNULL(T2.number_of_comments,0) AS number_of_comments
FROM (SELECT DISTINCT sub_id AS post_id
      FROM Submissions
      WHERE parent_id IS NULL) AS T1
         LEFT JOIN
     (SELECT DISTINCT parent_id AS post_id,
                      COUNT(DISTINCT sub_id) AS number_of_comments
      FROM Submissions
      GROUP BY parent_id) AS T2 ON T1.post_id = T2.post_id
ORDER BY T1.post_id;
```