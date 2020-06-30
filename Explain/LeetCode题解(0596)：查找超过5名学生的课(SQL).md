# LeetCode题解(0596)：查找超过5名学生的课(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/classes-more-than-5-students/)（简单）

| 解法        | 执行用时       |
| ----------- | -------------- |
| Ans 1 (SQL) | 209ms (67.93%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```sql
SELECT class
FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;
```