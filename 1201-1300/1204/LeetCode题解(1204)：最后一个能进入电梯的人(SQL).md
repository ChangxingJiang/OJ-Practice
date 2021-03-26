# LeetCode题解(1204)：最后一个能进入电梯的人(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/last-person-to-fit-in-the-elevator/)（中等）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 724ms (54.25%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT person_name
FROM (SELECT person_name, @now := @now + weight AS weight
      FROM Queue,
           (SELECT @now := 0) AS T1
      ORDER BY turn
) AS T2
WHERE weight <= 1000
ORDER BY weight DESC
LIMIT 1;
```

