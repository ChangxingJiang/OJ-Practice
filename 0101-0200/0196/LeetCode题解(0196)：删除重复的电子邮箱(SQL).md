# LeetCode题解(0196)：删除重复的电子邮箱(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/delete-duplicate-emails/)（简单）

| 解法        | 执行用时         |
| ----------- | ---------------- |
| Ans 1 (SQL) | 1208ms (>49.28%) |

> 应注意删除和查询不能再同一张表

解法一（先通过GROUP BY检索出需要移除的ID，再使用DELETE...WHERE...移除）：

```sql
DELETE
FROM person
WHERE Id NOT IN (
    SELECT Id
    FROM (SELECT MIN(Id) AS Id FROM person GROUP BY Email) AS a
);
```