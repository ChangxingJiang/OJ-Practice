# LeetCode题解(0584)：寻找用户推荐人(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/find-customer-referee/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 371ms (46.02%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT name
FROM customer
WHERE referee_id IS NULL
   OR referee_id <> 2;
```