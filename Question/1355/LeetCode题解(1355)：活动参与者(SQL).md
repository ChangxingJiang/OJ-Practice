# LeetCode题解(1355)：活动参与者(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/activity-participants/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 472ms (81.14%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT name AS activity
FROM Activities AS A
         LEFT JOIN
     (SELECT activity,
             COUNT(*) AS count
      FROM Friends
      GROUP BY activity) AS F ON A.name = F.activity
WHERE IFNULL(F.count, 0) != (SELECT IFNULL(count, 0)
                             FROM Activities AS A
                                      LEFT JOIN
                                  (SELECT activity,
                                          COUNT(*) AS count
                                   FROM Friends
                                   GROUP BY activity) AS F ON A.name = F.activity
                             ORDER BY count
                             LIMIT 1)
  AND IFNULL(F.count, 0) != (SELECT IFNULL(count, 0)
                             FROM Activities AS A
                                      LEFT JOIN
                                  (SELECT activity,
                                          COUNT(*) AS count
                                   FROM Friends
                                   GROUP BY activity) AS F ON A.name = F.activity
                             ORDER BY count DESC
                             LIMIT 1);
```