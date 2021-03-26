# LeetCode题解(0619)：只出现一次的最大数字(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/biggest-single-number/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 245ms (93.53%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT MAX(num) AS num
FROM (SELECT num
      FROM my_numbers
      GROUP BY num
      HAVING COUNT(num) = 1) AS T;
```