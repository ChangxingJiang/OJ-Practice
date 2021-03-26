# LeetCode题解(0180)：连续出现的数字(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/consecutive-numbers/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 372ms (59.20%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT DISTINCT log1.num AS 'ConsecutiveNums'
FROM logs AS log1,
     logs AS log2,
     logs AS log3
WHERE log1.id = log2.id - 1
  AND log2.id = log3.id - 1
  AND log1.num = log2.num
  AND log2.num = log3.num;
```