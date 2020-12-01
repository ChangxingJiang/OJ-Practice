# LeetCode题解(1440)：计算布尔表达式的值(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/evaluate-boolean-expression/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 1306ms (5.01%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT left_operand,
       operator,
       right_operand,
       CASE
           WHEN operator = '>' THEN
               IF((SELECT value FROM Variables WHERE name = E.left_operand)
                      >
                  (SELECT value FROM Variables WHERE name = E.right_operand), 'true', 'false')
           WHEN operator = '=' THEN
               IF((SELECT value FROM Variables WHERE name = E.left_operand)
                      =
                  (SELECT value FROM Variables WHERE name = E.right_operand), 'true', 'false')
           WHEN operator = '<' THEN
               IF((SELECT value FROM Variables WHERE name = E.left_operand)
                      <
                  (SELECT value FROM Variables WHERE name = E.right_operand), 'true', 'false')
           END AS value
FROM Expressions AS E;
```