# LeetCode题解(0620)：查找高评分的电影(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/not-boring-movies/)（简单）

| 解法        | 执行用时       |
| ----------- | -------------- |
| Ans 1 (SQL) | 169ms (36.29%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```mysql
SELECT *
FROM cinema
WHERE description != 'boring'
  AND mod(id, 2) = 1
ORDER BY rating DESC;
```