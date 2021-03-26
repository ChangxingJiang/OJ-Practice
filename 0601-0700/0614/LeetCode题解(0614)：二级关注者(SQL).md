# LeetCode题解(0614)：二级关注者(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/second-degree-follower/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 279ms (84.32%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT followee AS follower,
       COUNT(DISTINCT follower) AS num
FROM follow
GROUP BY followee
HAVING followee IN (SELECT DISTINCT follower FROM follow)
ORDER BY followee;
```