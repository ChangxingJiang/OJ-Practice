# LeetCode题解(0608)：树节点(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/tree-node/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 345ms (48.14%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT id, Type
FROM (SELECT id, 'Root' AS Type
      FROM tree
      WHERE p_id IS NULL) AS N
UNION
(SELECT id, 'Inner' AS Type
 FROM tree
 WHERE p_id IS NOT NULL
   AND id IN (SELECT DISTINCT p_id FROM tree))
UNION
(SELECT id, 'Leaf' AS Type
 FROM tree
 WHERE p_id IS NOT NULL
   AND id NOT IN (SELECT DISTINCT IFNULL(p_id, -1) FROM tree));
```