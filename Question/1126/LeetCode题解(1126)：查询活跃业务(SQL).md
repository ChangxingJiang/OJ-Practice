# LeetCode题解(1126)：查询活跃业务(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/active-businesses/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 650ms (43.36%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT E.business_id
FROM Events AS E
         LEFT JOIN
     (SELECT event_type, AVG(occurences) AS occurences
      FROM Events
      GROUP BY event_type) AS AVG ON E.event_type = AVG.event_type
WHERE E.occurences > AVG.occurences
GROUP BY E.business_id
HAVING COUNT(*) >=2;
```

