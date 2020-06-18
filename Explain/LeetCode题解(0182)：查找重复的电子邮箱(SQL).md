# LeetCode题解(0182)：查找重复的电子邮箱(SQL)

[题目链接](https://leetcode-cn.com/problems/duplicate-emails/)（简单）

| 解法        | 执行用时        |
| :---------- | --------------- |
| Ans 1 (SQL) | 250ms (>54.47%) |

解法一：

```SQL
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(*) > 1;
```