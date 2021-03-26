# LeetCode题解(1407)：排名靠前的旅行者(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/top-travellers/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 1380ms (5.15%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT U.name,
       IFNULL(SUM(distance),0) AS travelled_distance
FROM Users U
         LEFT JOIN
     Rides AS R ON R.user_id = U.id
GROUP BY user_id
ORDER BY travelled_distance DESC, U.name;
```