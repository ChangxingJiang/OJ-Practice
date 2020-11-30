# LeetCode题解(0610)：判断三角形(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/triangle-judgement/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 213ms (45.16%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT x, y, z,
       IF(x + y > z AND x + z > y AND y + z > x, 'Yes', 'No') AS triangle
FROM triangle;
```

