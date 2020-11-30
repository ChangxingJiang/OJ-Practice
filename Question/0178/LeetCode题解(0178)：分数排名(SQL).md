# LeetCode题解(0178)：分数排名(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/rank-scores/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 205ms (92.81%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT `Score`,
       DENSE_RANK() over (ORDER BY `Score` DESC) AS `rANK`
FROM `Scores`;
```