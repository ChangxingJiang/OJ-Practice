# LeetCode题解(1613)：找到遗失的ID(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-missing-ids/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 295ms (56.92%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
WITH RECURSIVE A AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1
    FROM A
    WHERE n < 100
)

SELECT n AS ids
FROM A
WHERE n NOT IN (SELECT customer_id FROM Customers)
  AND n <= (SELECT MAX(customer_id) FROM Customers);
```