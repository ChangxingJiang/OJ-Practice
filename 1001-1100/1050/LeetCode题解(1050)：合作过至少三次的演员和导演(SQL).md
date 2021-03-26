# LeetCode题解(1050)：合作过至少三次的演员和导演(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/actors-and-directors-who-cooperated-at-least-three-times/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 275ms (69.19%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(timestamp) >= 3;
```