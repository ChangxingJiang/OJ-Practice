# LeetCode题解(1435)：制作会话柱状图(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/create-a-session-bar-chart/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 320ms (34.97%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT '[0-5>' AS bin,
       COUNT(*) AS total
FROM Sessions
WHERE duration BETWEEN 0 AND 299
UNION
SELECT '[5-10>',
       COUNT(*)
FROM Sessions
WHERE duration BETWEEN 300 AND 599
UNION
SELECT '[10-15>',
       COUNT(*)
FROM Sessions
WHERE duration BETWEEN 600 AND 899
UNION
SELECT '15 or more',
       COUNT(*)
FROM Sessions
WHERE duration >= 900;
```