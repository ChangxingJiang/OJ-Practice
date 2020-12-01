# LeetCode题解(1264)：页面推荐(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/page-recommendations/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 396ms (43.06%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT DISTINCT page_id AS recommended_page
FROM Likes
WHERE user_id IN (SELECT user1_id AS friend
                  FROM Friendship
                  WHERE user2_id = 1
                  UNION
                  SELECT user2_id AS friend
                  FROM Friendship
                  WHERE user1_id = 1)
  AND page_id NOT IN (SELECT page_id
                      FROM Likes
                      WHERE user_id = 1);
```